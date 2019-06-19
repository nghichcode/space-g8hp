https://jekyllrb.com/docs/installation/

Installation
Jekyll is a Ruby Gem that can be installed on most systems.

RequirementsPermalink
Ruby version 2.4.0 or above, including all development headers (ruby version can be checked by running ruby -v)
RubyGems (which you can check by running gem -v)
GCC and Make (in case your system doesn’t have them installed, which you can check by running gcc -v,g++ -v and make -v in your system’s command line interface)


INSTALL

Install a full Ruby development environment

#Install Jekyll and bundler gems
gem install jekyll bundler

````Fix Some bug
chcp 850

#Create a new Jekyll site at ./myblog
jekyll new myblog

#Change into your new directory
cd myblog

#Build the site and make it available on a local server
bundle exec jekyll serve

Now browse to http://localhost:4000


SOME BEAUTY THEME
http://alperenbozkurt.net/JBlog/