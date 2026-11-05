Q: What is the purpose of the `"use strict"` directive in JavaScript and what risk does omitting it introduce?
A: `"use strict"` forces the engine into modern ES5+ mode, disabling legacy permissive behaviors. Without it, misspelled variable assignments (e.g., `usrRole = "Admin"`) create unintended global variables on `window`/`globalThis`, polluting global memory and causing subtle state-overwriting bugs.

```js
"use strict";
// Assigning undeclared variables throws ReferenceError instead of creating globals
// usrRole = "Admin"; // ReferenceError
```

---

Q: What are the best practices for choosing between `const`, `let`, and `var`?
A: Use `const` by default for bindings that won't be reassigned. Use `let` only when variable re-assignment is required (e.g., loop counters) within a block scope (`{}`). Completely avoid `var` due to scope leakage and `undefined` hoisting bugs.

```js
const API_URL = "https://api.example.com"; // Fixed binding
let attempts = 0; // Re-assignable
attempts++;
```

---

Q: What are the main production risks of using `var` instead of `let`/`const`?
A: 1. **No Block Scope:** `var` leaks outside `if`/`for` blocks, potentially overwriting outer variables.
2. **Unsafe Hoisting:** Accessing a `var` before declaration yields `undefined` instead of throwing a `ReferenceError`.
3. **Re-declaration:** `var` allows silent re-declarations without throwing syntax errors.

```js
if (true) {
  var leaked = "I leak outside block scope!";
}
console.log(leaked); // Accessible outside!
```

---

Q: Why is explicit type conversion preferred over implicit type coercion in JS?
A: Explicit conversion (`Number()`, `String()`, `Boolean()`) makes intent clear and self-documented. Implicit coercion is prone to calculation bugs—for example, the `+` operator favors string concatenation when one operand is a string, whereas `-` forces numeric conversion.

```js
const concatResult = "10" + 2; // "102" (string concatenation)
const mathResult = "10" - 2;   // 8 (numeric subtraction)
const explicitNum = Number("10") + 2; // 12 (safe)
```

---

Q: Why should strict equality (`===`) always be used instead of loose equality (`==`)?
A: Strict equality (`===`) checks both data type and value without performing type coercion. Loose equality (`==`) attempts implicit type conversions, leading to unexpected truths like `"0" == false`, `"" == 0`, or `[] == false`, which can compromise input validation and security checks.

```js
const input = "0";
console.log(input === 0); // false (Safe)
console.log(input == 0);  // true (Risky coercion)
```

---

Q: When should you use Nullish Coalescing (`??`) instead of logical OR (`||`)?
A: Use `||` when you want any *falsy* value (`0`, `""`, `false`, `null`, `undefined`, `NaN`) to trigger the fallback default. Use `??` when `0`, `""`, or `false` are considered valid business data, as `??` only falls back for `null` and `undefined`.

```js
const settings = { volume: 0 };
const volBad = settings.volume || 50;  // 50 (Incorrect: 0 was overwritten)
const volGood = settings.volume ?? 50; // 0 (Correct: 0 preserved)
```

---

Q: What risk does the `fall-through` behavior in a `switch` statement pose?
A: Omitting a `break` statement in a `switch` case causes execution to immediately fall through to subsequent cases regardless of whether their condition matches, executing unwanted code blocks.

```js
const role = "ADMIN";
switch (role) {
  case "ADMIN":
    console.log("Admin Access");
    // Missing `break;` will cause "User Access" to print too!
  case "USER":
    console.log("User Access");
}
```

---

Q: What happens if an infinite loop occurs in a single-threaded JavaScript environment?
A: Because JS runs on a single main thread (Event Loop), an infinite loop completely blocks the Event Loop. The page freezes, UI interactions stop working, and the browser throws a "Page Unresponsive" prompt.

```js
// Dangerous: Missing break condition
// while (true) { /* blocks Event Loop */ }
```

---

Q: Why shouldn't Arrow Functions (`() => {}`) be used as object methods or constructors?
A: Arrow functions do not have their own `this` binding (they inherit `this` lexically from the outer scope) and lack `.prototype` / `[[Construct]]` internal slots. Using them as methods causes `this` to point to the outer/global object (`undefined` or `window`), and using `new` with them throws a `TypeError`.

```js
const user = {
  name: "Alex",
  getNameBad: () => this.name, // undefined (inherits outer `this`)
  getNameGood() { return this.name; } // "Alex"
};
```

---

Q: Why is `null >= 0` evaluated as `true`, while `null == 0` evaluates as `false`?
A: Relational operators (`>=`, `>`, `<`) convert `null` to the number `0` (evaluating `0 >= 0` -> `true`). Loose equality (`==`) follows a distinct ECMAScript specification rule where `null` only loosely equals `undefined` and undergoes no numeric coercion.

```js
console.log(null > 0);  // false
console.log(null == 0); // false
console.log(null >= 0); // true
```

---

Q: What is the difference in numeric conversion between `null` and `undefined`?
A: `null` represents explicit absence of value and converts to `0`. `undefined` represents an uninitialized or unknown state and converts to `NaN`. Any mathematical operation on `NaN` propagates `NaN`.

```js
console.log(Number(null));      // 0
console.log(Number(undefined)); // NaN
console.log(null + 5);          // 5
console.log(undefined + 5);     // NaN
```

---

Q: How does Automatic Semicolon Insertion (ASI) create bugs with multiline `return` statements?
A: ASI automatically inserts a semicolon `;` immediately after `return` if a line break follows. This causes the function to execute `return;` (returning `undefined`) and ignore any object or expression placed on the next line.

```js
function getUser() {
  return
  {
    name: "Alex"
  };
}
console.log(getUser()); // undefined!
```

---

Q: Why is `NaN === NaN` evaluated as `false` and how should `NaN` be accurately checked?
A: According to the IEEE 754 standard, `NaN` (Not-a-Number) represents an undefined numeric result and is never equal to any value, including itself. To safely check for `NaN`, use `Number.isNaN(val)` or `Object.is(val, NaN)`.

```js
console.log(NaN === NaN);       // false
console.log(Number.isNaN(NaN)); // true
```

---

Q: How do `let`/`const` behave regarding scope, hoisting, and the Temporal Dead Zone (TDZ)?
A: `let` and `const` are block-scoped (`{}`). Although their declarations are hoisted during compilation, they remain uninitialized in the TDZ (from block entry until the actual declaration line). Accessing them inside the TDZ throws a `ReferenceError`.

```js
{
  // console.log(a); // ReferenceError: Cannot access 'a' before initialization
  let a = 10;
  console.log(b); // undefined (var is hoisted and auto-initialized)
  var b = 20;
}
```

---

Q: How does short-circuit evaluation work for `||` and `&&` operators?
A: Logical operators evaluate left-to-right and return the actual value of the last evaluated operand, not a Boolean:
- `A || B`: Evaluates `A`. If `A` is *truthy*, returns `A`; otherwise evaluates and returns `B`.
- `A && B`: Evaluates `A`. If `A` is *falsy*, returns `A`; otherwise evaluates and returns `B`.

```js
console.log("Alex" || "User"); // "Alex"
console.log("" || "User");     // "User"
console.log(0 && "User");      // 0
console.log(1 && "User");      // "User"
```

---

Q: What are the step-by-step coercion rules for the Abstract Equality Comparison algorithm (`==`)?
A: 1. If types match, perform strict comparison (`===`).
2. `null == undefined` returns `true`.
3. If comparing a `number` and a `string`, convert the string to a `number`.
4. If one operand is a `boolean`, convert it to a `number` (`true` -> 1, `false` -> 0).
5. If comparing an `object` to a primitive, convert the object via `valueOf()` or `toString()`.

```js
console.log("0" == false); // true ("0" -> 0, false -> 0, 0 == 0)
```

---

Q: What are the 6 *falsy* values in JavaScript?
A: `false`, `0`, `""` (empty string), `null`, `undefined`, and `NaN`.

```js
// All evaluate to false in boolean contexts:
console.log(Boolean(0));        // false
console.log(Boolean(""));       // false
console.log(Boolean(null));     // false
```

---

Q: What are the quick explicit syntax patterns for casting values to Number, Boolean, and Integer in JS?
A: - To Number: `+val` or `Number(val)`
- To Boolean: `!!val` or `Boolean(val)`
- To Integer parsing: `parseInt(val, 10)` (always pass radix 10)

```js
const num = +"42";          // 42 (number)
const bool = !!"text";      // true (boolean)
const intVal = parseInt("42px", 10); // 42 (number)
```