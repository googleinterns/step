# GitHub Repo Setup

Follow this walkthrough to setup your GitHub repo.

You can return to this walkthrough anytime by running this command:

```bash
teachme ~/step/walkthroughs/week-1-setup/github-setup-walkthrough.md
```

Click the `Start` button to start the walkthrough!

## Getting Started

[Git](https://git-scm.com/) is a distributed [version control](https://en.wikipedia.org/wiki/Version_control)
system, which lets you track changes to your files and collaborate with others.
[GitHub](https://github.com/) is a Git repository host, which means that it's a
website that allows you to store your repository and let others access it.
This is useful to release code as open source, or to use the advanced collaboration tools with a team.
You're going to use GitHub to store your projects.

## Register

If you already have a GitHub account, you can skip this step.

Go to [GitHub](https://github.com/) and register for an account.

Make sure you use your own email address here, not your `@google.com` account!

## Unlink Google's Repo

When you ran the command `git clone https://github.com/googleinterns/step.git`,
you downloaded the official repository to your Cloud Shell worksapce.

Right now, this repository still points to Google's GitHub account instead of yours.
To fix that, you're first going to remove the pointer to Google's repo.

Make sure you're inside the git repository you just cloned for the rest of
this walkthrough:

```bash
cd ~/step
```

Now to unlink this directory from Google's repo, execute this command:

```bash
git remote remove origin
```

## Create a GitHub Repository

On [GitHub](https://github.com/), click on the `+` in the top-right and click on
`new repository`. This will take you to a page to create your repo on GitHub.

1.  Enter a repository name. Something like `step` or
    `my-portfolio` is a fine name.
2.  Set your repo to public. This allows anyone to see your code.
3.  Click the green `create repository` button!

At this point you should have an empty repo.

## Link Your Repo

In your GitHub repo page, find your repo's URL. It should start with `https://`
and end in `.git`, like
`https://github.com/your-username/your-repo-name.git`. Copy that URL.

To link this local copy to your GitHub project, execute this command:

```bash
git remote add origin YOUR_URL_HERE
```

Then to store this directory in your repo, run this command:

```bash
git push -u origin master
```

This should prompt you for your username/password the first time that
you're pushing to GitHub. If your GitHub account is set up with two-factor
authentication, you'll need to create an [API Key](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) and use that instead of a password.

If you'd like Git to store the username/password for pushing to GitHub, change this setting:

```bash
git config credential.helper store
```

You should now see this code in your repo on GitHub!

## Add Collaborators

You'll be sending the code you write to your host for review, so your host
needs access to your repo.

To give your host access to your repo, add them as a collaborator.

1.  Navigate to your repo's page in GitHub.
1.  Go to the `Settings` tab.
1.  Select `Collaborators`. (*Note*: If you don't see this,
    look for `Manage Access` -> `Invite a Collaborator` instead)
1.  Add your host using their GitHub username or email address (you can send
them a quick message to confirm their Github username).

Your host can now help with code reviews.

## Require Pull Requests

When you write code, you're going to use **pull requests** to do code reviews.
To prevent accidentally modifying the code without going through a code review,
set your repo to require pull requests.

1.  Go to your GitHub repo page.
2.  Click the `Settings` tab.
3.  Select `Branches`.
4.  Click the `Add rule` button.
5.  Type `master` into the `Branch name pattern` text box.
6.  Select `Require pull request reviews before merging` and `Include
    administrators`.
7.  Select `Dismiss stale pull request approvals when new commits are pushed`.
8.  Click `Create`.
9.  Click `Save changes`.

## Tell git Who You Are

Before you can do anything else with git, you need to tell it who you are, so
it knows who to attribute commits to. First set your email (make sure to use
the same email as your GitHub account, and not your `@google.com` one):

```bash
git config --global user.email "you@example.com"
```

and then your name:

```bash
git config --global user.name "Your Name"
```

## Modify README

To test that everything is connected, modify your
<walkthrough-editor-open-file filePath="step/README.md">README.md</walkthrough-editor-open-file>
file.

This file contains the content that shows in your repo's GitHub page.
Change it to say "This repo contains [your name]'s portfolio and
STEP projects."

The `README.md` file now belongs to you. You should feel free to customize it
and make it your own!

## Push Your Changes

To save your changes to your repo, first create a branch:

```bash
git checkout -b YOUR_BRANCH_NAME
```

(You can use anything you want for `YOUR_BRANCH_NAME`. Something like
`[YourName]Development` is fine.)

Add the `README.md` file to the set of changes you want to upload:

```bash
git add README.md
```

Then create a commit which describes the changes you just made:

```bash
git commit -m "Update the README.md file to describe the repo."
```

Finally, push all of your changes to the shared repo:

```bash
git push origin YOUR_BRANCH_NAME
```

Your changes are now stored in a branch on your repo. Follow the instructions
[here](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
for creating a pull request to send your changes to your host for review.

## Congratulations!

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

After your host reviews your changes and you merge your pull request, you're
done with the GitHub repo setup!

The next walkthrough will introduce the Google Cloud Shell environment. Run this
command when you're ready:

```bash
teachme ~/step/walkthroughs/week-1-setup/intro-walkthrough.md
```
