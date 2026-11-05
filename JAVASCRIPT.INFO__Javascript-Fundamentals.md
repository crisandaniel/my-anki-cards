Q: What is the primary purpose of the `"use strict"` directive in JavaScript and what production risk does omitting it carry?
A: `"use strict"` forces the engine to execute code in modern ES5+ mode, disabling legacy permissive syntax. Without it, mispelling a variable name during assignment (e.g., `usrRole = "Admin"`) silently creates a new global variable on `window`/`globalThis`, polluting global memory and potentially overwriting state.

```js
"use strict";

let userRole = "Guest";
// With "use strict", assigning an undeclared variable throws ReferenceError:
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

Q: What are the recommended selection guidelines for `const`, `let`, and `var`?
A: - `const` (~90% default): Use for any variable whose binding/reference will not be reassigned.
- `let`: Use exclusively when the value must be reassigned (e.g., loop counters, state flags) within block scope (`{}`).
- `var` (Avoid): Has function scope and suffers from unpredictable hoisting.

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
A: 1. **No Block Scope:** `var` leaks outside `if`/`for` blocks and can overwrite outer variables.
2. **Undefined Hoisting:** Accessing a `var` before its declaration returns `undefined` instead of throwing an error, masking logic bugs.

```js
if (true) {
  var leakedVar = "Visible outside block!";
  let blockVar = "Isolated in block!";
}

console.log(leakedVar); // "Visible outside block!"
// console.log(blockVar); // ReferenceError: blockVar is not defined
```

---

Q: What is the Temporal Dead Zone (TDZ) and how does `let`/`const` hoisting differ from `var`?
A: TDZ is the period between entering a scope and reaching the line where a `let` or `const` variable is declared. Although `let` and `const` declarations are hoisted at compile time, they remain uninitialized in the TDZ; accessing them inside the TDZ throws a `ReferenceError`. Conversely, `var` is hoisted and automatically initialized with `undefined`.

```js
// TDZ (Temporal Dead Zone):
// console.log(score); // ReferenceError: Cannot access 'score' before initialization
let score = 100;
```

---

Q: How does internal object mutability work with `const`?
A: `const` guarantees that the variable reference itself cannot be rebound, but it does not make the content of objects or arrays immutable.

```js
const settings = { theme: "dark" };
settings.theme = "light"; // Allowed! (Internal mutation)
// settings = { theme: "light" }; // TypeError: Assignment to constant variable.
```

---

Q: Why is explicit type conversion preferred over implicit type coercion in production?
A: Explicit conversion (`Number()`, `String()`, `Boolean()`) is clear and self-documenting. Implicit coercion produces unexpected results: the `+` operator performs string concatenation if any operand is a string (`"10" + 2` -> `"102"`), whereas `-` forces numeric subtraction (`"10" - 2` -> `8`). Unconverted HTML form inputs (always strings) cause severe math bugs.

```js
const rawInput = "42";

// Explicit conversion (Safe)
const age = Number(rawInput); // 42 (number)

// Unary plus conversion
const count = +rawInput; // 42 (number)

// Implicit coercion risk:
const concatResult = "10" + 2; // "102" (string)
const mathResult = "10" - 2;   // 8 (number)
```

---

Q: Why does `typeof null` return `"object"` and how do you accurately check for `null`?
A: `typeof null === "object"` is a historical bug from JS's first version, where values were stored on 32-bit units with `000` type tags denoting objects (and `null` was the null pointer `0x00`). To check if a value is strictly `null`, use strict equality: `val === null`.

```js
console.log(typeof null); // "object"
console.log(null === null); // true
```

---

Q: How do `null` and `undefined` differ during numeric conversion?
A: `null` represents an explicit absence of value and converts to `0`. `undefined` represents an uninitialized or unknown value and converts to `NaN`.

```js
console.log(Number(null));      // 0
console.log(Number(undefined)); // NaN

console.log(null + 5);      // 5
console.log(undefined + 5); // NaN
```

---

Q: Why should strict equality (`===`) always be used instead of loose equality (`==`)?
A: `===` checks both value and data type without implicit coercion. `==` converts operands to a common type first, producing dangerous truths such as `"0" == false`, `"" == 0`, or `[] == false`, which can compromise validation logic and security checks.

```js
const inputString = "0";

console.log(inputString === 0); // false (Safe)
console.log(inputString == 0);  // true (Risky)
```

---

Q: Why is `null >= 0` evaluated as `true` while `null == 0` evaluates as `false`?
A: Relational operators (`>`, `<`, `>=`) convert `null` to the number `0`, resulting in `0 >= 0` (`true`). However, the loose equality operator `==` follows an ECMAScript specification rule stating that `null` only loosely equals `undefined` and undergoes no numeric coercion against `0`.

```js
console.log(null > 0);  // false
console.log(null == 0); // false
console.log(null >= 0); // true
```

---

Q: How does string comparison work on numeric strings like `"2" > "12"`?
A: When both operands are strings, JavaScript performs a lexicographical comparison character-by-character according to Unicode values (`'2'` > `'1'`), without converting the strings to numbers.

```js
console.log("2" > "12"); // true
```

---

Q: What is the main operational difference between logical OR (`||`) and Nullish Coalescing (`??`)?
A: `||` falls back to the right operand for any *falsy* value (`0`, `""`, `false`, `null`, `undefined`, `NaN`). `??` falls back only when the left operand is strictly `null` or `undefined`, preserving valid business data like `0` or `""`.

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
A: Logical operators evaluate left-to-right and return the actual value of the last evaluated operand:
- `A || B`: Evaluates `A`. If `A` is *truthy*, short-circuits and returns `A`. If *falsy*, evaluates and returns `B`.
- `A && B`: Evaluates `A`. If `A` is *falsy*, short-circuits and returns `A`. If *truthy*, evaluates and returns `B`.

```js
console.log("Alex" || "User"); // "Alex"
console.log("" || "User");     // "User"
console.log(0 && "User");      // 0
console.log(1 && "User");      // "User"
```

---

Q: When should you use a `switch` statement instead of `if...else if` chains?
A: `switch` is preferred when evaluating a single expression against a discrete set of fixed values (e.g., HTTP status codes, Redux actions). In many JS engines, large `switch` statements can be optimized internally using lookup tables rather than evaluating sequential `else if` conditions.

---

Q: What is the risk of missing a `break` statement in a `switch` block?
A: Omitting `break` causes a *fall-through* effect: execution continues sequentially into subsequent cases regardless of whether their condition matches, executing unintended logic.

```js
const role = "ADMIN";

switch (role) {
  case "ADMIN":
    console.log("Admin Access");
    break; // Prevents fall-through to "USER"
  case "USER":
    console.log("User Access");
    break;
}
```

---

Q: How does matching work in a `switch` statement regarding data types?
A: `switch` uses strict equality (`===`) for case matching. Matching a string value `"1"` against a numeric case `1` will fail.

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

Q: What happens to the Event Loop when an infinite loop executes in JavaScript?
A: Because JS operates on a single main thread, a synchronous infinite loop never yields control back to the execution stack. It completely blocks the Event Loop, preventing UI rendering, click handlers, or asynchronous callbacks from processing, freezing the page ("Page Unresponsive").

```js
// Loop execution model:
for (let i = 0; i < 3; i++) {
  console.log(`Step ${i}`);
}

let count = 0;
do {
  count++;
} while (count < 0); // Runs guaranteed at least once (count = 1)
```

---

Q: How can you break out of deeply nested loops in JavaScript?
A: A standard `break` only exits the innermost loop. To break out of an outer loop simultaneously, use a syntactic Label statement.

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

Q: What are the main differences between Function Declarations, Function Expressions, and Arrow Functions?
A: - **Function Declaration:** Hoisted completely; can be called before its definition in code.
- **Function Expression:** Assigned to a variable; not hoisted.
- **Arrow Function:** Concise syntax; lacks its own `this`, `arguments`, `.prototype`, or `[[Construct]]`.

```js
// Function Declaration (Hoisted)
console.log(add(2, 3)); // 5
function add(a, b) {
  return a + b;
}

// Arrow Function (Callback)
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2); // [2, 4, 6]
```

---

Q: Why shouldn't Arrow Functions be used as object methods or constructor functions?
A: Arrow functions do not bind their own `this` context (they inherit `this` lexically from the parent scope). Used as object methods, `this` points to the outer/global object instead of the instance. They also lack `.prototype` and internal `[[Construct]]` slots, so calling them with `new` throws a `TypeError`.

```js
const user = {
  name: "Alex",
  getNameBad: () => this.name,        // undefined
  getNameGood() { return this.name; } // "Alex"
};

const Person = (name) => { this.name = name; };
// new Person("Alex"); // TypeError: Person is not a constructor
```

---

Q: How do `.bind()`, `.call()`, and `.apply()` affect Arrow Functions?
A: Because Arrow Functions establish `this` lexically at creation time and do not have a local `this` binding, methods like `.bind()`, `.call()`, or `.apply()` are ignored when called on an Arrow Function. They cannot mutate an Arrow Function's `this` context.