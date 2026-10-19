# Part B: Reflection

## 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?

I wrote 8 tests in Part A. The `kitchen.py` file has about 45 lines of code. The ratio is about 8 tests to 45 lines of production code.

## 2. When was your bar red for the longest time, and what made it last so long?

The red bar lasted the longest when I worked on mixed-unit addition. It was difficult because grams and ounces need a conversion rate before they can be added correctly. I had to make the `Converter`, `Quantity`, and `Sum` work together.

## 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?

I used **Fake It** for the first multiplication test by using a fixed result. I used **Triangulate** by adding another multiplication test with a different number. This helped me find the real multiplication formula.

I used **Obvious Implementation** for simple functions such as `grams()` and `ounces()`. I think these choices were right because they helped me develop the code step by step.

## 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?

All items on my test list are completed. I would keep the tests because they check important behaviors, such as multiplication, equality, addition, conversion, and mixed-unit calculations.

## 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?

Probably not. I did not think about this method at the beginning. It appeared naturally when I needed to convert quantities to the target unit. TDD helped me create the method based on the tests.

## 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?

In Part 0, testing after writing the code felt easier because I already knew how the code worked. In Part A, writing tests first was more difficult because I had to think about the expected behavior before writing the code.

However, the Part A tests helped shape my design. The tests for different units, addition, and conversion helped me understand that I needed `Quantity`, `Sum`, and `Converter` to work together.