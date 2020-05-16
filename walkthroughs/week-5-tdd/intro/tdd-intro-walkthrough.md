# Test Driven Development - Intro

## Getting Started

So far, you've built a portfolio page using both server and client code.

This week, you'll learn about test-driven development, which allows you to make
changes to code more safely. You'll also practice writing code that uses data
structures and algorithms.

You can return to this walkthrough anytime by running this command:

```bash
teachme ~/step/walkthroughs/week-5-tdd/intro/tdd-intro-walkthrough.md
```

Click the **Start** button to begin!

## Unit Testing

As you wrote your code last week, you probably tested it manually by:

1. running a server
2. interacting with your HTML page
3. submitting data
4. confirming that your code did what you expected

That is a lot of work to confirm one little change, and it becomes less
effective the larger your project becomes. Imagine it's not just you working on
this project, but a team of 10 people. How would you know that your change
didn't break something they added?

[Unit testing](https://en.wikipedia.org/wiki/Unit_testing) is a way to confirm
that the small pieces that make up your code (e.g. each function) work as
expected. Each **unit test** is a small program that calls some code from your
project then tests the actual output against the expected output.

For example, open the
<walkthrough-editor-open-file
    filePath="step/walkthroughs/week-5-tdd/intro/src/main/java/com/google/sps/Greeter.java">
  Greeter.java
</walkthrough-editor-open-file>
file. This class creates greeting messages. How can you confirm that this code
does what you expect?

Next, open the
<walkthrough-editor-open-file
    filePath="step/walkthroughs/week-5-tdd/intro/src/test/java/com/google/sps/GreeterTest.java">
  GreeterTest.java
</walkthrough-editor-open-file>
file. This class contains a unit test that confirms the behavior of the
`Greeter` class.

To run the test, `cd` into the `intro` directory and then execute this command:

```bash
mvn test
```

This command will compile all the code, and then run the tests in the
`GreeterTest` class. When it finishes, you should see something like:

```none
Results :
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
BUILD SUCCESS
```

This means that there is one test (`"Test run: 1"`) and that all tests passed
(`"Failures: 0"`). In other words, this means that the code is working how it
was expected to work.

## Test-driven Development

[Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development)
is used by many teams at Google. Test-driven development uses tests to define
the correct behavior for code, and then developers write code that passes the
tests.

For example, add this function to the
<walkthrough-editor-open-file
    filePath="step/walkthroughs/week-5-tdd/intro/src/test/java/com/google/sps/GreeterTest.java">
  GreeterTest.java
</walkthrough-editor-open-file>
file:

```java
@Test
public void testGreetingTrimsWhitespace() {
  Greeter greeter = new Greeter();

  String greeting = greeter.greet("   Ada   ");

  // Whitespace should be trimmed
  Assert.assertEquals("Hello Ada", greeting);
}
```

This function tests whether whitespace is trimmed from the `name` parameter.
Save the file and run the tests again:

```bash
mvn test
```

You should now see this output:

```none
Results :
Failed tests:   testGreetingWhitespace(com.google.sps.GreeterTest): expected:<Hello [Ada]> but was:<Hello [   Ada   ]>
Tests run: 2, Failures: 1, Errors: 0, Skipped: 0
BUILD FAILURE
```

This tells you that the `testGreetingWhitespace` test failed. The expected
output was `"Hello Ada"` but the actual output was `"   Hello Ada   "`. This
means something in the code is not working as expected.

The problem is that the `Greeter` class is not removing the extra whitespace.
Modify the
<walkthrough-editor-open-file
    filePath="step/walkthroughs/week-5-tdd/intro/src/main/java/com/google/sps/Greeter.java">
  Greeter.java
</walkthrough-editor-open-file>
file to trim the whitespace. After doing that, run the tests again. You should
see them passing now.

Tests are useful for defining new desired behavior, and to confirm that new
code doesn't break existing behavior.

**Practice:** If you want more practice, try writing a new test that confirms
that symbols like `@#$%` are removed from the input, and then modify the code so
the tests pass.

## JUnit

The code this week uses a testing library called **JUnit**. You can learn more
about it by running through [this tutorial](https://howtodoinjava.com/junit-4/). Reference material is available [here](https://junit.org/junit4/). Note that there is a version of JUnit called JUnit 5 but most of our work at Google still uses JUnit 4 so that is what we will be using in this program.

If you want to learn how to test for something with JUnit, try including that
in your search. For example, if you want to test that a method throws an
exception, you might search for "JUnit confirm exception thrown".



## Mocking

One of the major challenges of developer testing is that the tests that you write should be fast so that you can run them frequently and quickly.
The problem is that this is not always easy when the code you are testing interacts with other systems (e.g. an external database) that could have high latency, or not be available from your test environment at all.

One solution would be for your test to create a test database for your code to interact with but that is likely to also be quite time consuming.

To resolve this problem, all programming languages with unit testing libraries offer libraries to do was is called "mocking". [Mock objects](https://en.wikipedia.org/wiki/Mock_object) are lightweight, in-memory objects that simulate or mimic the behavior of real objects in ways that make it easy (or at least easier) to test. For this program, we will be using the [Mockito](https://site.mockito.org/) framework that we use for Java mocking at Google.

This [tutorial](https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html#1) shows an example of how to mock a List object using Mockito. Of course, mocking a List is unnecessary since it is already in-memory and fast but it serves as a good, easy-to-understand example of how mocking works.


## Next Steps

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You've finished the introductory walkthrough!

Start the project by running the project walkthrough:

```bash
teachme ~/step/walkthroughs/week-5-tdd/project/calendar-walkthrough.md
```