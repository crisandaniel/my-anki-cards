<!-- note_key: 0682d5f54be7 -->
<!-- note_type: AnkiOpsQA -->
<!-- tags: data_types -->
Q: How many types are in js and what are they?
A: 7 primitives \+ 1 non-primitive (object)

```js
// primitives
typeof 123.12       // 'number' (1)
typeof 1234n        // 'bigint' (2)
typeof "true"       // 'string' (3)
typeof true         // 'boolean' (4)
typeof null         // 'object' (5) 
typeof undefined    // 'undefined' (6)
typeof Symbol("id") // 'symbol' (7)

// non primitive data type
typeof Math         // 'object' (8)
```

`null` is not an object; it's an error in `typeof`. It's a standalone type that has only one value: `null`

---

<!-- note_key: 5ffe29a1d09e -->
<!-- note_type: AnkiOpsQA -->
<!-- tags: data_types -->
Q: What are the 2 `special numeric values`
A: - `Infinity` = division by 0
```js
alert( 1/0 ); // Infinity
```
- `NaN` - computational error - a result of an incorrect or an undefined mathematical operation
```js
alert( "string" / 2 ); // NaN
```

---

<!-- note_key: 2bcdeb006600 -->
<!-- note_type: AnkiOpsQA -->
<!-- tags: data_types -->
Q: What does `NaN is sticky` means
A: It means if there is a NaN in a math expression it propagates to the end result

```js
alert ( 3 \* 3 \+ "a" / 2 ); // NaN because "a"/2 is NaN
```

---

<!-- note_key: 6ef21be2f302 -->
<!-- note_type: AnkiOpsQA -->
<!-- tags: data_types -->
Q: What is the difference between `null` and `undefined`
A: While both are data types `null` means "unknown", "nothing", "empty". `null` data type has only one value: `null` and `undefined` means that "value is not assigned".

`null` is assigned to a variable intentionally while `undefined` is assigned by JS

To INITIALIZE a variable with nothing use `null` while `undefined` is reserved as the `default value for unassigned things` 
```js
let a = null // it's initialized
let b; // gets undefined by default
```

---

<!-- note_key: 77e05b8a4086 -->
<!-- note_type: AnkiOpsQA -->
<!-- tags: data_types -->
Q: Why `typeof null` prints `object`?
A: This is an officially recognized error in `typeof` but kept for compatibility.

To demonstrate it's not an object we know that any object has properties. If we try to set a property to `null` it will throw an error

```js
let myNullObj = null;
myNullObj.name = "my null object";

TypeError: Cannot set properties of null (setting 'name')
```

---

<!-- note_key: e6a15175d963 -->
<!-- note_type: AnkiOpsQA -->
<!-- tags: data_types -->
Q: What does `typeof function() {}` return and why?
A: ```js
typeof function() {}
'function'
```
While 'function' is still an object `typeof` returns `function` so you know you can call it with ().

---

<!-- note_key: 9af161c672c8 -->
<!-- note_type: AnkiOpsQA -->
<!-- tags: data_types -->
Q: What type does `NaN` have?
A: ```js
typeof NaN
'number' // although NaN means "Not A Number"
```

---

<!-- note_key: 104386593eae -->
<!-- note_type: AnkiOpsQA -->
<!-- tags: data_types -->
Q: Is `NaN == NaN` ?
A: `NaN` is a placeholder for computational error. JS cannot establish if 2 computational errors are the same.

```js
NaN === NaN
false

NaN == NaN
false

"6 0"/2 
NaN

"6 0" / 2 == "8 0" / 2 // although both are NaN
false
 
Number.isNaN(" 6 0 " / 2) // Use Number.isNaN instead
true
```
