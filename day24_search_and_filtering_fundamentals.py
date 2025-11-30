# Day 24 – Adding Search and Filters to Our Django Blog

Today we learn how to add a Search feature to our Day10 Blog without breaking anything.
We will add:

- A search bar in the homepage
- ?q= text filtering (title contains)
- ?author= filtering (exact match)

Example:
    /?q=hello
    /?author=alice
    /?q=hello&author=alice

This teaches:
- How Django request.GET works
- How to filter QuerySets safely
- How to update templates without breaking existing tests
- How to extend a real project step-by-step

We do NOT modify anything that Day 10–23 tests rely on.
We add features *on top* only.


