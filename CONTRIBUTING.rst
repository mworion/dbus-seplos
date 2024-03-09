====================================
 Contributing to dbus-seplos
====================================

There are many ways you can contribute to dbus-seplos.

* **Contributing documentation** in the form of python doc, and documents like this.
* **Using dbus-seplos;** reporting bugs and patches into the issue tracker.
 * https://github.com/mworion/dbus-seplos/issues
* **Following up on current Issues** by posting comments in the issue tracker  
  and/or submitting pull requests.

Contributing Overview
---------------------

Because we are using Github the process for contributing is as follows:

1. We acquire a github account. 
 * https://github.com
2. We fork mworion/dbus-seplos's repo.
 * https://github.com/mworion/dbus-seplos
3. We git clone our Fork to a local working copy on our own machine. 
 * git clone https://github.com/<YOUR ID HERE>/dbus-seplos
4. We create development branches in our own working copy. 
 * git checkout -b Issue31
5. We code by adding/modifying/deleting documentation or code
6. We commit 
 * git commit -m "#31 Fix involved: blah blah blah"
7. We push our fix branches to our Forked repo. 
 * git push origin Issue31
8. On Github we submit a pull request from this forked branch into 
   mworion/dbus-seplos's main repo.

Very small Git Example of Contributing
--------------------------------------

You can experiment with what works for you from a git perspective. The following 
is just some examples of what a developer can do.

1. Created a Fork in my own github space.
2. Cloned my Forks master branch.
 * git clone git@github.com:mworion/dbus-seplos.git
3. Add skyfield reference to my local git repo.
 * git remote add skyfield git@github.com:mworion/dbus-seplos.git
 * git fetch dbus-seplos
 * git branch -r  <-- Shows me what remote repo's I have fetched references from
4. Make sure my master is up to date with the main repo.
 * git checkout master
 * git rebase dbus-seplos/master
5. Fork a development branch
 * git checkout -b fix42
6. Commit the change
 * git commit -m "#42 I fixed by ....."
7. Push the development branch to GitHub
 * git push origin fix42
8. Login to GitHub and issue a Pull request for my fix42 branch

From this point you can actually keep fetching from dbus-seplos repo as follows:

1. Make sure things are up to date
 * git checkout master
 * git rebase dbus-seplos/master
2. create a new development branch
 * git checkout -b issue43

You could even do this:

* git fetch dbus-seplos
* git checkout -b issue43 dbus-seplos/master
