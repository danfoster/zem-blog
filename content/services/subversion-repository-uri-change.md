Title: Subversion repository URI change
Date: 2010-08-11 08:15
Author: dan
Category: Services
Tags: Services, subversion
Slug: subversion-repository-uri-change

The location of subversion repositories at zem.org.uk has changed. Until
now all repositories have been available via
svn+ssh://zem.org.uk/srv/svn/\<repo\> on port 222. This has now been
changed to https://zem.org.uk/svn/\<repo\>.

### What do I need to do?

If you make use of the CLI subversion client, you should be able to run
the following command while in the base of your working copy:

     $ svn switch --relocate svn+ssh://zem.org.uk/srv/svn/<repo> https://zem.org.uk/svn/<repo>

For other clients, please see it's documentation. If you are having
issues switching the repository and have no local modifications it may
be simpler to checkout a new working copy and remove the old copy.

### Why the Change?

-   Running subversion on a non-default ssh port causes confusion for
    many users.

-   In the past subversion over https would silently store passwords in
    plaintext, therefore svn over ssh with keypairs was preferred. Many
    subversion clients are now able to store passwords in an encrypted
    fashion as well as warning the user if they can only store it in
    plaintext
    ([http://blogs.open.collab.net/svn/2009/07/subversion-16-security-improvements.html][]).

-   Subversion over https gives the possibility of finer control of
    permissions.

  [http://blogs.open.collab.net/svn/2009/07/subversion-16-security-improvements.html]:
    http://blogs.open.collab.net/svn/2009/07/subversion-16-security-improvements.html
