# Static site generator

By Frank William Hammond Espinosa (Frankwii). Created it following the course "Build a static site generator" on [boot.dev]("https://www.boot.dev"), but with a twist.

## Usage
This software converts a directory of Markdown files into static HTML and launches them to localhost (port 8888).

To use it, simply replace the contents of the directory `static/` with the desired assets of the HTML project (images, css...) and add your Markdown files into the `content/`  directory following the directory structure you wish to have in your page: the Markdown file to be displayed at address `localhost:8888/address1/.../addressN` should be at `contents/address1/.../addressN/index.md` (example files come by default in directories `static/` and `content/`; see those for clarification).

Once the files are in place, simply execute the `main.sh` script with any shell (Bash or zsh are the most popular, but it should work in any POSIX-compliant shell) having Python 3 installed.

## It's purely functional
In the code you will find no loops, no variable mutation and only pure functions (except, of course, those regarding input/output). Just map-reduce and recursion all the way, baby.
### Why?
#### Why functional programming?
The course in [boot.dev]("https://www.boot.dev") is presented as a follow-up to a first course on Functional Programming (FP). Even in that first course, they say that using loops or mutating *some* things *sometimes* is fine, since programming in a purely functional fashion is usually way harder.

However, I wanted to challenge myself and I tried following a strictly imperative style. After successfully doing it, I think I grasped much better how one can program like this.

#### Why Python?
Python is certainly not the best language out there for FP purposes. However, the course is supposed to be followed in Python and it is the language which I feel most comfortable programming in. And for the purpose of this project (which is learning the fundamentals of FP) it is as good as any!
