# Additional Features

## Getting Started

In this walkthrough, we'll be adding two additional features to
our comments functionality:

-   Letting the user select the number of comments displayed
-   Letting the user delete all comments

You can return to this walkthrough anytime by running this command:

```bash
teachme ~/step/walkthroughs/week-3-server/step-6-additional-features-walkthrough.md
```

Click the **Start** button to begin!

## Requesting a Number of Comments

If many comments have been created, they can start to take up far too much space
on your portfolio page. To help avoid this, you will let the user pick a
maximum number of comments to fetch and display.

### Server Support

First, you'll update your servlet to accept a maximum number of comments
in the request for `doGet()`. Check out SubtractionServlet.java in the
`subtraction-game` directory for an example of how to read HTTP request
params in your servlet. Your servlet should then limit the number of comments
it returns based on the request parameter.

### Query String Param

For HTTP GET requests, the typical way to include request parameters
is in the [query string](https://en.wikipedia.org/wiki/Query_string)
of the url. For now, hard-code a value for your request param into
the query string of your fetch request url.

Run a dev server to make sure that you now correctly display a limited
number of comments.

### User Input

Now it's time to let the user select how many comments should be fetched
and displayed. Add a section above or below the comments in index.html
that prompts the user and provides a way for them to set a maximum number
of comments. You may choose to let the user enter the number directly or
pick from a set of options; we recommend investigating
[number input](https://www.w3schools.com/tags/att_input_type_number.asp)
and [select](https://www.w3schools.com/tags/tag_select.asp) tags to
decide which you like best.

Whichever HTML tag you choose, modify script.js to replace your previously
hard-coded query string value with the
[value](https://www.w3schools.com/tags/att_value.asp) of that element.

### Refreshing Comments

Now that the user can change how many comments should be displayed, you'll
need to give them a way to refresh the comments section when they make
a selection. This can be a button, or you may want to use the HTML
[onchange](https://www.w3schools.com/tags/att_onchange.asp) attribute.
Make sure that you clear out the old comments when inserting the
new response into the DOM!

Run a dev server to make sure that your new feature is working properly.

## Deleting Comments

Any time you have a way to add data to a database, you should have a way
to delete that data. For now, you'll simply provide an option to delete
all existing comments.

### Server Support

Add a new `DataServlet` for the url `/delete-data`. Implement the
`doPost()` method to delete the contents of your datastore (check out the
[documentation](https://cloud.google.com/appengine/docs/standard/java/datastore/creating-entities#Deleting_entities)
to help you get started). Your servlet can just return an empty response
when it is done.

### Deleting Comments

You can use the same `fetch()` API to send POST as well as GET requests:
check out the
[request documentation](https://developer.mozilla.org/en-US/docs/Web/API/Request)
on MDN. Add a new function to your script.js which sends a POST request to
the `/delete-data` url. Once you get the response back from the server, you
should call your function to fetch comments from the server so that the
now-deleted comments are removed from the page; you can either use
`Promise.then()` to chain the calls, or use `await` for your POST request.

*Note: it might look a little strange to make a GET request to `/data`
when we know we will just be deleting all the comments, but it's usually
a good idea to let the server be the
[single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth).
This prevents our web page from getting out of sync with the datastore
as we add more complex behavior.*

Finally, add a button to index.html below your comment section which calls
your comment deletion function. Run a dev server to make sure that
your comments are deleted and cleared from the page.

## Pull Request

Congratulations! You have added two important features to your comment
functionality. After making sure that everything is working properly in
a dev server, create a pull request and send it to your host for
review. Then go back to the comments walkthrough to continue:

```bash
teachme ~/step/walkthroughs/week-3-server/comments-walkthrough.md
```
