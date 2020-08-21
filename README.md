<img height="120px" src="img/wordcounter.jpg" />

# Wordcount

In this assignment you will use your knowledge of Python basic strings, arithmetic, file reading, and dictionaries to create a command line utility to count the words in the text files in the `books` directory &mdash; ([small.txt](./books/small.txt) and [alice.txt](./books/alice.txt)).

Complete the command-line python program named `wordcount.py` so that it will count the number of words in a text file using optional flags named `--count` and `--topcount`.

## Example
```console
$ python wordcount.py --count books/alice.txt
"'tis : 1
"--said : 1
"come : 2
"coming : 1
"edwin : 1
"french, : 1
"he's : 1
"how : 2
"i : 8
"i'll : 2
"it" : 2
"keep : 1
"let : 1
"much : 1
"poison" : 1
"purpose"?' : 1
```

```console
$ python wordcount.py --topcount books/alice.txt
Top 20 most frequent words in books/alice.txt
the : 1605
and : 766
to : 706
a : 614
she : 518
of : 493
said : 421
it : 362
in : 352
was : 333
you : 265
i : 261
as : 249
that : 222
alice : 221
her : 208
at : 206
had : 176
with : 169
all : 155
```

## Part A
For the `--count` flag, implement a `print_words()` function that counts how often each word appears in the text and prints:

    word1 : count1
    word2 : count2
    ...
  
Print the above list in order, sorted alphabetically by word (Python will sort punctuation to come before letters, which is fine &mdash; do not strip out punctuation). Store all the words as lowercase (i.e., 'The' and 'the' count as the same word).

## Part B
For the `--topcount` flag, implement a `print_top()` function similar to `print_words()`, but which prints just the top 20 most common words sorted so the **most common** word is first, then the next most common, and so on.

## Testing with Unittest
This assignment also has separate unit tests to help you during development. The unit tests are located in the `tests` folder; you should not modify these.  Make sure all unit tests are passing before you submit your solution. You can invoke the unit tests from the command line at the root of your project folder:
```console
$ python -m unittest discover tests
```
You can also run these same tests using the `Test Explorer` extension built in to the VSCode editor, by enabling automatic test discovery.  This is a really useful tool and we highly recommend to learn it.

https://code.visualstudio.com/docs/python/testing#_test-discovery

- Test framework is `unittest`
- Test folder pattern is `tests`
- Test name pattern is `test*`

## Submitting your work
To submit your solution for grading, you will need to create a github [Pull Request (PR)](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).  Refer to the `PR Workflow` article in your course content for details.
