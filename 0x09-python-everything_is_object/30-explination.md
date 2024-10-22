In CPython, small integers (typically between -5 and 256) are cached and reused to improve performance. Here's how many ``int`` objects are created by your script:

1. Execution of the first line (``a = 1``):

When you execute ``a = 1``, Python checks if the integer ``1`` is already cached. Since``1`` is within the cached range, it reuses the existing object. Therefore, **0 new ``int`` objects** are created on this line.
Output for 103-line1.txt:`0`

2. Execution of the second line (``b = 1``):

Similar to the first line, when you execute ``b = 1``, Python again finds that ``1`` is already cached and reuses the same object. Thus, **0 new ``int`` objects **are created on this line as well.
Output for 103-line2.txt:`0`
