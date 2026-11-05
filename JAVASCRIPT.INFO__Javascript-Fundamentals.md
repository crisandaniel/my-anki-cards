<!-- note_key: f703e0961fb9 -->
<!-- note_type: AnkiOpsQA -->
Q: What does the "use strict" directive do in JavaScript and why is it recommended?
A: Enabled at the beginning of a script or function, strict mode disables legacy permissive behaviors (such as automatic creation of undeclared global variables or silent failures on assignment) and forces cleaner, safer code.

---

<!-- note_key: 1d99c71c78ef -->
<!-- note_type: AnkiOpsQA -->
Q: What is Automatic Semicolon Insertion (ASI) and why is relying on it risky?
A: ASI is the mechanism by which the JS engine automatically inserts semicolons `;` at line breaks. Relying on it is risky because in certain edge cases (e.g., lines starting with `[` or `(`) ASI can fail, causing unexpected runtime errors.

---

<!-- note_key: 53b8d6346b35 -->
<!-- note_type: AnkiOpsQA -->
Q: What is the difference in scope and hoisting between `let`/`const` and `var`?
A: `let` and `const` have block scope (`{}`) and reside in the Temporal Dead Zone (TDZ), meaning they cannot be accessed before declaration. `var` has function/global scope, is hoisted without TDZ, and is implicitly initialized with `undefined`.

---

<!-- note_key: fa30801132bb -->
<!-- note_type: AnkiOpsQA -->
Q: What does the `const` keyword guarantee in JavaScript?
A: `const` guarantees that the variable reference cannot be reassigned. It does not guarantee immutability of object or array contents, which can still be mutated internally.

---

<!-- note_key: 9e5d54b006a1 -->
<!-- note_type: AnkiOpsQA -->
Q: What are the 8 data types in JavaScript?
A: 7 primitives: `number`, `string`, `boolean`, `null`, `undefined`, `symbol`, `bigint`, and 1 complex type: `object`.

---

<!-- note_key: 69ba9bf29826 -->
<!-- note_type: AnkiOpsQA -->
Q: What is the historical anomaly of the `typeof` operator regarding `null`?
A: `typeof null` returns `"object"`, even though `null` is a separate primitive type. This is a legacy bug preserved for backward compatibility.

---

<!-- note_key: 557b8a61a340 -->
<!-- note_type: AnkiOpsQA -->
Q: How does the Nullish Coalescing operator (`??`) differ from the logical OR operator (`||`)?
A: The `||` operator treats all *falsy* values (`0`, `""`, `false`, `null`, `undefined`, `NaN`) as missing values, whereas `??` treats only *nullish* values (`null` and `undefined`) as missing values.

---

<!-- note_key: 414f95ab7832 -->
<!-- note_type: AnkiOpsQA -->
Q: What is the difference between prefix (`++x`) and postfix (`x++`) increment operators?
A: Prefix (`++x`) increments the value and returns the new value. Postfix (`x++`) increments the value but returns the old value (prior to incrementation).

---

<!-- note_key: fadef6319664 -->
<!-- note_type: AnkiOpsQA -->
Q: How do Function Declarations differ from Function Expressions regarding hoisting?
A: Function Declarations are processed during the compilation phase (fully hoisted) and can be called before their definition line. Function Expressions are created dynamically only when execution reaches that line.

---

<!-- note_key: 6426f056357c -->
<!-- note_type: AnkiOpsQA -->
Q: Why is `null >= 0` evaluated as `true`, but `null == 0` as `false`?
A: Relational operators (`>=`) convert `null` to the number `0` (resulting in `0 >= 0` -> `true`). Loose equality (`==`) follows a special rule where `null` equals only `undefined` and does not convert to a number.

---

<!-- note_key: d0cc7b50f94a -->
<!-- note_type: AnkiOpsQA -->
Q: What is the result of `Number(null)` compared to `Number(undefined)`?
A: `Number(null)` returns `0` (explicit absence of value), while `Number(undefined)` returns `NaN` (uninitialized/unknown value).

---

<!-- note_key: 87099991cba2 -->
<!-- note_type: AnkiOpsQA -->
Q: Why is `Boolean("0")` `true`, but `"0" == false` is also `true`?
A: `Boolean("0")` is `true` because any non-empty string is *truthy*. On the other hand, `"0" == false` applies numeric coercion to both operands (`0 == 0`), which evaluates to `true`.

---

<!-- note_key: 7336f29e8d48 -->
<!-- note_type: AnkiOpsQA -->
Q: What issue does ASI cause when a `return` statement is followed by a new line?
A: ASI automatically inserts a semicolon `;` immediately after `return`, making the function return `undefined` and ignoring the code/object on the next line.

---

<!-- note_key: b074227f48a5 -->
<!-- note_type: AnkiOpsQA -->
Q: How does `NaN` behave in equality comparisons (`NaN === NaN`) and how should it be checked?
A: `NaN === NaN` evaluates to `false` (it is the only JS value not equal to itself). To check for `NaN`, use `Number.isNaN(val)` or `Object.is(val, NaN)`.

---

<!-- note_key: 45aa3892ee13 -->
<!-- note_type: AnkiOpsQA -->
Q: Why does the expression `1 && 2 ?? 3` throw a SyntaxError?
A: The JavaScript specification explicitly forbids combining `&&` or `||` directly with `??` without explicit parentheses (`(1 && 2) ?? 3`) to prevent priority ambiguity.

---

<!-- note_key: 4174ba39f6a2 -->
<!-- note_type: AnkiOpsQA -->
Q: What is the result of the comparison `"2" > "12"` and why?
A: It returns `true` because when both operands are strings, the comparison is done lexicographically (character by character based on Unicode values), and `'2'` is greater than `'1'`.

---

<!-- note_key: c6441d98f625 -->
<!-- note_type: AnkiOpsQA -->
Q: What is the step-by-step algorithm for Abstract Equality Comparison (`==`)?
A: 1. If types match, compare values strictly.
2. `null == undefined` evaluates to `true`.
3. If comparing `number` and `string`, convert the string to a `number`.
4. If one operand is `boolean`, convert it to a `number` (`true` -> 1, `false` -> 0).
5. If comparing an `object` with a primitive, convert the object to a primitive via `valueOf()` / `toString()`.

---

<!-- note_key: 501efea7665b -->
<!-- note_type: AnkiOpsQA -->
Q: What is the Temporal Dead Zone (TDZ)?
A: TDZ is the time frame between entering a block scope and the exact line where a `let` or `const` variable is declared and initialized. Accessing the variable during this window throws a `ReferenceError`.

---

<!-- note_key: 19b413c39c86 -->
<!-- note_type: AnkiOpsQA -->
Q: Why can't Arrow Functions be used as object methods or constructor functions?
A: 1. They lack their own `this` binding (they inherit `this` lexically from the outer scope).
2. They lack internal `[[Construct]]` and `.prototype` properties (cannot be called with `new`).
3. They do not bind an `arguments` object.

---

<!-- note_key: 4e21b5d67d38 -->
<!-- note_type: AnkiOpsQA -->
Q: How does short-circuit evaluation work for `A || B` and `A && B`?
A: Logical operators return the value of the last evaluated operand:
- `A || B`: If `A` is *truthy*, returns `A`; otherwise evaluates and returns `B`.
- `A && B`: If `A` is *falsy*, returns `A`; otherwise evaluates and returns `B`.

---

<!-- note_key: 199661db8652 -->
<!-- note_type: AnkiOpsQA -->
Q: What are the 6 *falsy* values in JavaScript?
A: `false`, `0`, `""` (empty string), `null`, `undefined`, and `NaN`.

---

<!-- note_key: ab8d003b1a7c -->
<!-- note_type: AnkiOpsQA -->
Q: How can you perform fast explicit type conversions to Number, Boolean, and Integer in JS?
A: - To Number: `+val` or `Number(val)`
- To Boolean: `!!val` or `Boolean(val)`
- To Integer parsing: `parseInt(val, 10)`
