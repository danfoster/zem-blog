Title: OpenVZ first impressions
Date: 2009-10-03 19:44
Author: dan
Category: Sysadmin
Tags: openvz, server
Slug: openvz-first-impressions

So I took the plunge last week and re-installed my dedicated server.
This time using openVZ for OS level visualization.

My main reason for this is that more people wanted shell access for
various reasons and therefore I wanted a more isolated environment. I've
got to say I'm generally impressed, although I still don't fully
understand the use of varous user\_beancounters for memory management.
Maybe if I stare at [this diagram][] long enough it will all make sense.

Hopefully I will get around to noting how I set things up, but for now I
must continue moving services to openvz containers.

  [this diagram]: http://maxgarrick.com/understanding-openvz-resource-limits/
