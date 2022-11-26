# Instructors

* Rob Hasker (many years through present)
* Gerald (Jerry) Thomas (Once a few years ago, again Winter 2022-2023)
* Josiah Yoder (many years through present)


## Description
This repo is for any materials you desire to share with other instructors of the course.  **This repo should NOT be shared with students**.

I plan to place all my labs in this repo.

## Installation of Markdown Rendering
The markdown rendering script was developed by Dr. Jim Lembke.

To convert the markdown files in this folder into HTML for Canvas, you will need  [Pandoc](https://pandoc.org/installing.html). (The Python package simply assumes Pandoc is available on the system path.)  You may find that installing a few Python packages is also required.

Please report any difficulties you have with installation to Josiah Yoder so these instructions can be improved.

**You must manually create the folder `bld`** with the root of the repository.

## Rendering Markdown
See the installation instructions above. You MUST have pandoc installed on your system and a `bld` folder in the root of your repo before running this script.

To render everything, run

```
cd Builder
python buildmd.py
```

This generates html files in the `bld/` folder. These HTML files can be copied to Canvas directly in the Rich Content Editor (RCE)'s HTML view.  However, any attachments or images must be manually uploaded to Canvas and relinked.

Jim reports that canvas.py works, but requires enough fiddling that it is NOT worthwhile in practice.  He has also explored embedding images into the generated HTML but sadly Canvas stripped these out, so the current script doesn't do that.

## Questions?
Ask Josiah. Or Jim. Or Rob. Or Jerry. We don't care who you ask, just ask, ask, ask!


## Contributing
Please push directly to main. But don't force-push.

You are welome to create a merge request if you *WANT* another instructor looking at your changes.

Where maintaining parallel versions of a lab is necessary, please prepend your name to your customized version, e.g. Lab2.yoder.md.  The main version of the lab is the one without an instructor's name.

## Authors and acknowledgment
As mentioned earlier, Jim Lembke wrote the script for Markdown to HTML translation.

Most labs in this course are the result of many years of collaboration between Rob Hasker and Josiah Yoder.  Some labs were loosely inspired by Jay Urbain Mark Hornick.

## License
TBD.
