# Test Driven Development - Calendar

**Prerequisite:** If you're new to test-driven development, make sure you read
the intro walkthrough first!

## Getting Started

This week, you will be creating an
[algorithm](https://en.wikipedia.org/wiki/Algorithm) to solve a hard problem -
scheduling meetings between multiple people.

To make this easier, you will be using test-driven-development to make sure
your algorithm handles the different cases correctly.

You can return to this walkthrough anytime by running this command:

```bash
teachme ~/step/walkthroughs/week-5-tdd/project/calendar-walkthrough.md
```

Click the **Start** button to begin!

## Scenario

Imagine you're working on the calendar team and are responsible for adding the
"find a meeting" feature. Using the existing API, you'll need to implement a
feature that given the meeting information, it will return the times when the
meeting could happen that day.

## Background

A meeting request has:

-   a name
-   a duration in minutes
-   a collection of attendees

For a particular time slot to work, all attendees must be free to attend the
meeting. When a query is made, it will be given a collection of all known
events. Each event has:

-   a name
-   a time range
-   a collection of attendees

A time range will give you the start time, the end time, and the duration of
the event. If you want to know more, open the
<walkthrough-editor-open-file
    filePath="step/walkthroughs/week-5-tdd/project/src/main/java/com/google/sps/TimeRange.java">
  TimeRange.java
</walkthrough-editor-open-file>
file.

## Objective

Your objective is to implement `query()` in the
<walkthrough-editor-open-file
    filePath="step/walkthroughs/week-5-tdd/project/src/main/java/com/google/sps/FindMeetingQuery.java">
  FindMeetingQuery.java
</walkthrough-editor-open-file>
file.

Your implementation must pass every test in `FindMeetingQueryTests.java` before
the feature will be considered complete. Keep in mind, if a test is failing, it
means that your code needs to change, not the test.

Ignore optional attendees for now.

To run the tests, `cd` into the `project` directory and then execute this
command:

```bash
mvn test
```

When all the tests pass, you can be confident that your code works!

## Writing more tests

To practice the principles of Test-Driven Development, it is now your turn to write some tests.

You are going to be adding some new functionality to your calendar, specifically, support for optional attendees for a meeting.

The basic functionality of optional attendees is that if one or more time slots exists so that both mandatory and optional attendees can attend, return those time slots. Otherwise, return the time slots that fit just the mandatory attendees.

Before implementing this feature, add some new tests to the <walkthrough-editor-open-file
    filePath="step/walkthroughs/week-5-tdd/project/src/test/java/com/google/sps/FindMeetingQueryTest.java">
  FindMeetingQueryTest.java
</walkthrough-editor-open-file>

file. Write one test for each of the following scenarios:

1. Based on `everyAttendeeIsConsidered`, add an optional attendee C who has an all-day event. The same three time slots should be returned as when C was not invited.
2. Also based on `everyAttendeeIsConsidered`, add an optional attendee C who has an event between 8:30 and 9:00. Now only the early and late parts of the day should be returned.
3. Based on `justEnoughRoom`, add an optional attendee B who has an event between 8:30 and 8:45. The optional attendee should be ignored since considering their schedule would result in a time slot smaller than the requested time.
4. No mandatory attendees, just two optional attendees with several gaps in their schedules. Those gaps should be identified and returned.
5. No mandatory attendees, just two optional attendees with no gaps in their schedules. `query` should return that no time is available.

Feel free to add additional tests for other scenarios that you think might be worth testing.

Then modify `query` to make those new tests (and the provided tests) pass.


## Optional Coding Challenge

**Note**: This part of the activity is not required but a challenge you can take on if you have the time:

Implement an optimized version of the optional attendee functionality: If no time exists for all optional and mandatory attendees, find the time slot(s) that allow mandatory attendees and the greatest possible number of optional attendees to attend.

## Pull Request

To get feedback on your code, create a pull request and send it to your host
for review.

Make sure your code is merged into your repo before the end of the week!

## Web Application

The code you wrote can be used in many contexts: from tests, from a desktop Java
application, from server-side Java, etc.

This project contains a bare-bones web application that uses HTML, JavaScript,
and a servlet to allow users to interact with the code you just wrote. This code
is already written!

You can imagine you worked on a team where you were responsible for the
algorithm, and somebody else was responsible for the web application that calls
your algorithm.

To run the web application, run a server:

```bash
mvn package appengine:run
```

Then open the web preview to view a webpage that shows a user interface that
provides access to the algorithm you wrote!

## Finishing Up

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You've created your own algorithm, used data structures to solve a complex
problem, and have seen how unit testing helped ensured everything works. That's
a lot for one week!

If you have time left over this week and you're looking for a challenge:

-   What's the algorithmic complexity of your algorithm?
-   What's another algorithm to solve this problem?
