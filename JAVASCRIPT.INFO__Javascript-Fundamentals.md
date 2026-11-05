Q: What is the primary purpose of the `"use strict"` directive in JavaScript and what production risk does omitting it carry?
A: `"use strict"` forces the engine to execute code in modern ES5+ mode, disabling legacy permissive behaviors and converting silent failures into explicit runtime errors. Without it, mispelling a variable name during assignment (e.g., `usrRole = "Admin"`) silently creates a new global variable on `window`/`globalThis`, polluting global memory and potentially overwriting application state.

```js
"use strict";

let userRole = "Guest";
// With "use strict", assigning an undeclared variable throws a runtime error:
// usrRole = "Admin"; // ReferenceError: usrRole is not defined
```

---

Q: What main legacy issues does `"use strict"` resolve in JavaScript?
A: 1. Blocks accidental creation of global variables when `let`/`const`/`var` is omitted (throws `ReferenceError`).
2. Prevents writing to read-only properties or non-extensible objects (throws `TypeError`).
3. Forbids duplicate parameter names in functions and reserves future keywords (`implements`, `interface`, `private`).

---

Q: How does Automatic Semicolon Insertion (ASI) create a bug with multiline `return` statements?
A: If the returned expression starts on a new line after `return`, ASI automatically inserts a semicolon `;` immediately after `return`. The function executes `return;` (returning `undefined`) and ignores the block below.

```js
function getPayload() {
  return
  {
    status: 200
  };
}

console.log(getPayload()); // undefined
```

---

Q: What are the selection criteria for `const`, `let`, and `var` in modern JavaScript?
A: - **`const` (~90% default):** Use for any variable whose reference binding must remain fixed. It prevents accidental reassignment.
- **`let`:** Use exclusively when the variable's value must be reassigned (e.g., loop counters, state flags) within block scope (`{}`).
- **`var` (Avoid):** Has function scope and suffers from unpredictable hoisting.

```js
// Fixed binding:
const API_URL = "https://api.example.com";
const userConfig = { timeout: 5000 };
userConfig.timeout = 10000; // Allowed (mutating contents), but `userConfig = {}` throws TypeError

// Re-assigned binding:
let attempts = 0;
attempts += 1;
```

---

Q: What risks are associated with using `var` instead of `let`/`const`?
A: 1. **No Block Scope:** `var` leaks outside `if`/`for` blocks, which can accidentally overwrite outer scope variables.
2. **Undefined Hoisting:** Accessing a `var` before its declaration returns `undefined` instead of throwing an error, masking logical bugs.
3. **Re-declaration:** `var x = 1; var x = 2;` is allowed without warnings, leading to accidental overwrites.

```js
if (true) {
  var leakedVar = "Visible outside IF block!";
  let blockVar = "Isolated in block!";
}

console.log(leakedVar); // "Visible outside IF block!"
// console.log(blockVar); // ReferenceError: blockVar is not defined
```

---

Q: What is the Temporal Dead Zone (TDZ) and how does `let`/`const` hoisting differ from `var`?
A: TDZ is the time window between entering a scope and reaching the exact line where a `let` or `const` variable is declared and initialized. Although `let` and `const` declarations are hoisted at compile time, they remain uninitialized in the TDZ; accessing them inside the TDZ throws a `ReferenceError`. Conversely, `var` is hoisted and automatically initialized with `undefined`.

```js
// TDZ (Temporal Dead Zone):
// console.log(score); // ReferenceError: Cannot access 'score' before initialization
let score = 100;
```

---

Q: How does internal object mutability work with `const`?
A: `const` guarantees that the variable's memory reference cannot be rebound to another value. However, it does **not** freeze the internal contents of objects or arrays referenced by that variable.

```js
const settings = { theme: "dark" };
settings.theme = "light"; // Allowed! (Internal mutation)
// settings = { theme: "light" }; // TypeError: Assignment to constant variable.
```

---

Q: Why is explicit type conversion preferred over implicit type coercion in production?
A: Explicit conversion (`Number()`, `String()`, `Boolean()`) is clear, predictable, and self-documenting. Implicit coercion produces unexpected results: the `+` operator favors string concatenation if any operand is a string (`"10" + 2` -> `"102"`), whereas `-` forces numeric subtraction (`"10" - 2` -> `8`). Unconverted HTML form inputs (always strings) cause mathematical calculation bugs.

```js
const rawInput = "42";

// Explicit conversion (Safe)
const age = Number(rawInput); // 42 (number)

// Unary plus conversion
const count = +rawInput; // 42 (number)

// Implicit coercion risks:
const concatResult = "10" + 2; // "102" (string)
const mathResult = "10" - 2;   // 8 (number)
```

---

Q: Why does `typeof null` return `"object"` and how do you accurately check for `null` in code?
A: `typeof null === "object"` is a historical bug from JavaScript's first implementation, where values were stored in 32-bit units with `000` type tags denoting objects (and `null` was represented as the null pointer `0x00`). To check if a value is strictly `null`, use strict equality: `val === null`.

```js
console.log(typeof null); // "object"
console.log(null === null); // true
```

---

Q: How do `null` and `undefined` differ during numeric conversion?
A: `null` represents an explicit absence of value and converts to numeric `0`. `undefined` represents an uninitialized or missing value and converts to `NaN` (Not-a-Number), which propagates `NaN` through any subsequent arithmetic operation.

```js
console.log(Number(null));      // 0
console.log(Number(undefined)); // NaN

console.log(null + 5);      // 5
console.log(undefined + 5); // NaN
```

---

Q: What is the asymmetry of `NaN !== NaN` and how should you check for NaN?
A: According to IEEE 754 standards, `NaN` represents an undefined numerical result. Because an invalid numerical result is not guaranteed to equal another invalid numerical result, `NaN` is not equal to any value, including itself (`NaN === NaN` is `false`). Use `Number.isNaN(val)` or `Object.is(val, NaN)` for accurate checks.

```js
console.log(typeof NaN);        // "number"
console.log(NaN === NaN);       // false
console.log(Number.isNaN(NaN)); // true
```

---

Q: Why should strict equality (`===`) always be used instead of loose equality (`==`)?
A: Strict equality (`===`) checks both value and data type without implicit coercion. Loose equality (`==`) attempts to convert operands to a common type first, producing counterintuitive results like `"0" == false` (`true`), `"" == 0` (`true`), or `[] == false` (`true`), which can compromise validation logic and security checks.

```js
const inputString = "0";

console.log(inputString === 0); // false (Safe)
console.log(inputString == 0);  // true (Risky)
```

---

Q: Why is `null >= 0` evaluated as `true` while `null == 0` evaluates as `false`?
A: Relational comparison operators (`>`, `<`, `>=`) convert `null` to the number `0`, resulting in `0 >= 0` (`true`). However, the loose equality operator `==` follows a specific ECMAScript rule: `null` only loosely equals `undefined` and undergoes no numeric coercion against `0`.

```js
console.log(null > 0);  // false
console.log(null == 0); // false
console.log(null >= 0); // true
```

---

Q: How does string comparison work on numeric strings like `"2" > "12"`?
A: When both operands are strings, JavaScript performs a lexicographical comparison character-by-character according to Unicode character codes (`'2'` > `'1'`), without converting the strings to numbers.

```js
console.log("2" > "12"); // true
```

---

Q: What is the difference between logical OR (`||`) and Nullish Coalescing (`??`)?
A: `||` falls back to the right operand for any *falsy* value (`0`, `""`, `false`, `null`, `undefined`, `NaN`). `??` falls back only when the left operand is strictly `null` or `undefined`, preserving valid business data like `0` (e.g., volume level 0) or `""`.

```js
const userSettings = { volumeLevel: 0 };

// Incorrect fallback with || (overwrites valid 0):
const volumeBad = userSettings.volumeLevel || 50; // 50

// Correct fallback with ?? (preserves 0):
const volumeGood = userSettings.volumeLevel ?? 50; // 0
```

---

Q: What happens if you combine `??` with `&&` or `||` without explicit parentheses?
A: The JavaScript specification throws a `SyntaxError` to prevent operator precedence ambiguity.

```js
// const result = 1 && 2 ?? 3; // SyntaxError: Unexpected token '??'
const result = (1 && 2) ?? 3; // 2
```

---

Q: How does short-circuit evaluation work for `||` and `&&` operators?
A: Logical operators evaluate left-to-right and return the actual value of the last evaluated operand, not a simple boolean:
- **`A || B`:** Evaluates `A`. If `A` is *truthy*, short-circuits and returns `A`. If *falsy*, evaluates and returns `B`.
- **`A && B`:** Evaluates `A`. If `A` is *falsy*, short-circuits and returns `A`. If *truthy*, evaluates and returns `B`.

```js
console.log("Alex" || "User"); // "Alex"
console.log("" || "User");     // "User"
console.log(0 && "User");      // 0
console.log(1 && "User");      // "User"
```

---

Q: When should you use a ternary operator (`?`) vs `if/else` vs `switch`?
A: - **Ternary (`?`):** Use exclusively for concise, single-line value assignments based on a condition.
- **`if / else`:** Use for complex multi-line logic or when performing side-effects (API calls, state updates).
- **`switch`:** Use when comparing a single expression against a discrete set of fixed values.

```js
const role = "ADMIN";
const access = role === "ADMIN" ? "Full" : "Limited"; // Single line assignment
```

---

Q: What are the main implementation pitfalls of `switch` statements?
A: 1. **Fall-through Effect:** Omitting `break` causes execution to flow sequentially into subsequent cases regardless of whether their conditions match.
2. **Strict Type Matching:** `switch` uses strict equality (`===`), so string `"1"` will not match numeric case `1`.

```js
const inputCode = "1";

switch (inputCode) {
  case 1:
    console.log("Number");
    break;
  default:
    console.log("Type mismatch"); // Executes default! ("1" !== 1)
}
```

---

Q: Why can a `switch` statement offer performance advantages over an `if...else if` chain?
A: A `switch` evaluates a single expression against discrete constant values. In many JS engines, large `switch` statements can be optimized internally using lookup tables, whereas `else if` chains must evaluate conditions sequentially one by one.

---

Q: How do loop selections differ between `for`, `while`, and `do...while`?
A: - **`for`:** Use when the exact number of iterations is known or when iterating array indices.
- **`while`:** Use when the iteration count is unknown, depending on a dynamic condition evaluated *before* each pass.
- **`do...while`:** Use when the loop body must execute *at least once guaranteed*, evaluating the condition *after* the first run.

```js
let count = 0;
do {
  count++;
} while (count < 0);
console.log(count); // 1 (Executed once)
```

---

Q: What happens to the Event Loop when a synchronous infinite loop executes?
A: Because JavaScript runs on a single main thread, a synchronous infinite loop never yields control back to the execution stack. It completely blocks the Event Loop, preventing UI rendering, click events, or asynchronous callbacks from executing, freezing the page ("Page Unresponsive").

---

Q: How can you break out of deeply nested loops in JavaScript?
A: A standard `break` only terminates the innermost loop. To break out of an outer loop simultaneously, attach a syntactic Label to the outer loop and pass it to `break`.

```js
outerLoop: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i === 1 && j === 1) {
      break outerLoop; // Terminates the outer loop!
    }
  }
}
```

---

Q: What are the key operational differences between Function Declarations, Function Expressions, and Arrow Functions?
A: - **Function Declaration:** Fully hoisted; can be called before its definition in code.
- **Function Expression:** Defined dynamically when execution reaches its line; not hoisted.
- **Arrow Functions (`() => {}`):** Concise syntax; lacks its own `this`, `arguments`, `.prototype`, or constructor capability.

```js
// Function Declaration (Hoisted)
console.log(add(2, 3)); // 5
function add(a, b) {
  return a + b;
}

// Arrow Function (Concise callback)
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2); // [2, 4, 6]
```

---

Q: Why shouldn't Arrow Functions be used as object methods?
A: Arrow Functions do not bind their own `this` context; they inherit `this` lexically from the outer scope in which they were defined. When used as an object method, `this` points to the outer context (`window` or `undefined` in strict mode) rather than the object instance.

```js
const user = {
  name: "Alex",
  getNameBad: () => this.name,        // undefined
  getNameGood() { return this.name; } // "Alex"
};

console.log(user.getNameBad());  // undefined
console.log(user.getNameGood()); // "Alex"
```

---

Q: Why can't Arrow Functions be used as constructors with `new`?
A: Arrow Functions lack the internal `[[Construct]]` slot and do not possess a `.prototype` property. Attempting to call an Arrow Function with `new` throws a `TypeError`.

```js
const Person = (name) => { this.name = name; };
// new Person("Alex"); // TypeError: Person is not a constructor
```

---

Q: How do `.bind()`, `.call()`, and `.apply()` affect Arrow Functions?
A: Because Arrow Functions bind `this` lexically at creation time and have no local `this` binding, methods like `.bind()`, `.call()`, or `.apply()` are ignored. They cannot alter an Arrow Function's `this` context.

---

Q: Do Arrow Functions have their own `arguments` object?
A: No. Arrow Functions do not have a local `arguments` object. If `arguments` is accessed inside an Arrow Function, it will resolve to the `arguments` object of the nearest non-arrow enclosing function. To capture arguments in an Arrow Function, use rest parameters (`...args`).

```js
const showArgs = (...args) => {
  console.log(args); // [1, 2, 3]
};
showArgs(1, 2, 3);
```