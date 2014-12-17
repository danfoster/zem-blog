---
title: Writing Puppet Modules
category: sysadmin
tags: cfgman, puppet
---

Writing and testing puppet modules in a way that can easily be used by others
can be overwhelming. Puppetlabs guide, [Beginner's Guide to
Modules](https://docs.puppetlabs.com/guides/module_guides/bgtm.html), is a good
start, but doesn't go in detail on particular areas. The rest of this post contains (hopefully) useful information to fill in these gaps.

## Aim to publish your module.

From the start, you should aim to writing your module in such a way that it
could be published to the [Puppet Forge](http://forge.puppetlabs.com). This encourages 
you to follow best practises which, while having a steeper learning curve, will
produce much more maintainable code. You also get that extra fuzzy feeling that
you've helped others in your organisation and the wider world.

To get started, use the following command to generate some boilerplate:

{% highlight bash %}
puppet module generate danfoster-mynewmodule
mv danfoster-mynewmodule mynewmodule
{% endhighlight %}

Note the format of the module name is that of `author-modulename` and then we
rename the directory to just contain the modulename. I've heard rumours that
this 2nd step won't be needed in future versions of puppet, but you'll have to
do it for now.

This will produce a bunch of boiler plate code and some example Documentation to get you started.

## Config / Code seperation

Your module should not have any site local configuration data in so it can
easily be reused. Class parameters should be put in a separate file
(`params.pp`) with sensible
defaults where possible. The users of your module can then overwrite your
parameters in their class definition or hiera data.

## Unit testing

Unit testing is just as important for puppet modules as it is for software.
At first it may feel like you're duplicating your efforts by writing both your modules and unit tests. Once your module becomes more complex, for example with any sort of conditional logic in it, they become invaluable. It's best to start writing your unit tests from the start to ease the pain.

[RSpec](http://rspec.info/) is the de facto testing tool for Ruby and
[rspec-puppet](http://rspec-puppet.com/) provides a suite of test to run
against your puppet manifests.
There is a still a significant amount of
boilerplate code that has to be written. Luckily Puppetlabs have created
[puppetlabs_spec_helper](https://github.com/puppetlabs/puppetlabs_spec_helper) to easy some of this pain. A good guide on using `puppet_spec_helper` can be found [here](http://puppetlabs.com/blog/the-next-generation-of-puppet-module-testing).

## Acceptance Testing

Acceptance testing

### Testing workflow

While developing a module and/or tests, you probably don't want to be provisioning the VM every time. You also probably want to be able to get a shell on the test VM to see what's going on. You can do this by using the following workflow

. For the first time, provision the box and run the tests (but do not destroy the VM) by running: `BEAKER_destroy=no bundle exec rake beaker`
. For subsequent runs, run the tests using: BEAKER_destroy=no BEAKER_provision=no bundle exec rake beaker`
. If you want to SSH to the VM for diagnostic, run: `( cd .vagrant/beaker_vagrant_files/default.yml; vagrant ssh )`
