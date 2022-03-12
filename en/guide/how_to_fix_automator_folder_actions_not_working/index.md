# How To Fix Automator Folder Actions Not Working


Welcome to what’s probably going to be my shortest AppleToolBox post for a long time. Today, I’m just going to show you how to fix Automator folder actions that have stopped working. Skip to the next section for a quick and easy solution to this problem!

I have been uploading a lot of [Automator](https://appletoolbox.com/the-best-automator-routines-for-mac/) and [Shortcuts](https://appletoolbox.com/the-best-iphone-shortcuts-2021-edition/) content over the last month in preparation for the Shortcuts release on macOS Monterey. While writing these posts and using these apps, I ran into a super frustrating issue.

**A folder action I had created in Automator wasn’t running.**

At first, I thought maybe I had just created a broken Automator routine. But I noticed that whenever I ran it manually from within the Automator app, it would work fine. It wasn’t that my folder action was bad – it was that, for some reason, it wasn’t running on its own. In other words, it wasn’t automating.

I tried to find a solution to this issue online and could find next to no information on this issue. It makes sense, considering that Automator isn’t a very popular app. But this only made things even more frustrating.

Eventually, though, I was able to find a fix using an app I had never heard of – **Folder Actions Setup**. That’s the fix I’m going to be sharing with you.

To be clear, this is the **only** solution we’re going to be covering. I’m not going to show you how to fix a folder action that isn’t working because it wasn’t created properly. We’re specifically going to be focusing on Automator folder actions that won’t run unless you force them to.

For other issues, I recommend sharing screenshots of your folder action on the appropriate [StackExchange](https://apple.stackexchange.com/) and Reddit forums! They’ll be able to read your workflow and spot the issue.

Alright, let’s get started!

## How to fix Automator folder actions that aren’t working

To fix this issue, we’re going to use the Folder Actions Setup app. This is an app that lets you manage all of the Automator folder actions you’ve created. To find it, press **cmd** + **spacebar** to open Spotlight, then type “Folder Actions Setup” and press **return**.

![img](https://appletoolbox.com/wp-content/uploads/2021/08/Screen-Shot-2021-08-17-at-1.08.58-AM-540x370.png)

Once you do that, this app will open:

![img](https://doraemonj.github.io/pics/Screen-Shot-2021-08-17-at-1.11.11-AM-540x361.png)

You’ll notice a few things here.

First, some of the folders listed might be red. If a folder is red, it means that there aren’t any folder actions attached to that folder. Even if a folder has an action tied to it that isn’t turned on, it still won’t appear red.

Second, you’ll notice that there are checkmarks *everywhere*. Each checkmark is used to control which folder actions are activated and which aren’t. If every box has a check in it, then your folder action probably is running. It just isn’t working properly, which means you need to keep editing it in Automator.

If you’re like me, then you’ll notice that a checkmark might be missing next to the folder action you are trying to get to work. As you’ve probably guessed already, go ahead and add a check next to that workflow! Then, test that action and see if your workflow is working now.

### Here’s a quick process you can follow to make sure your folder action is activated:

1. Make sure that the **Enable Folder Actions** checkbox has a check in it. It’s located in the top-left of the window.
2. Find the folder that your folder action should be attached to on the left-hand side of the window. In my example above, the action I was trying to get to work was attached to the Downloads folder, so I selected that folder in the left-hand pane.
3. If you can’t find the folder you’re looking for, click the **+** icon in the bottom-left of the screen. Then, navigate through Finder to find the folder you’re looking for and click **Open**. That will add it to the list of folders in the left-hand pane of this window.
4. Make sure there is a checkmark next to the folder that contains the folder action you are trying to get to run. If there isn’t, click the box next to the folder’s title to add a checkmark.
5. Select that folder from the left-hand pane. When you do, you’ll see a list of all of the folder actions that have been attached to this folder. There will be a checkbox next to each action. Make sure there is a checkmark next to each folder action you want to run. Conversely, remove checkmarks from the action that you don’t want to run.
6. If you want to delete a folder action, select that action in the right-hand pane of the Folder Actions Setup window and click the **–** icon at the bottom of the right-hand pane. Don’t click the **–** icon on the bottom-left side of the window or you will remove a folder from the list, not the action.
7. To edit a folder action, select it and click the **Edit Workflow** button at the bottom-right of the window. That will open the folder action in Automator.

## Your Automator folder actions should be working now!

And that’s it! That’s probably a bit more detail than most of you need to get your Automator folder actions working again. I wanted to make sure that everyone could find the solution to their issue here, though, so hopefully, this solved your issue!

Again, if you weren’t able to fix your folder action using this method, I recommend sharing it on a [StackExchange](https://apple.stackexchange.com/) forum. The users there are pretty good about helping you find a quick solution to your problem.

For more problem-solving, guides, and news on all things Apple, check out the rest of [the AppleToolBox blog](https://appletoolbox.com/).

See you next time!
