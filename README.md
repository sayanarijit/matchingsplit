## subliment

Fix subtitles by referencing a supplement text.

Example

```python
from subliment import fix

fix(["this", "is", "a", "good", "thing"], "this must be a good thing")
# ["this", "must be", "a", "good", "thing"]

fix(["this", "must", "be", "a", "good", "thing"], "this is a good thing")
# ["this", "is", "is", "a", "good", "thing"]
```
