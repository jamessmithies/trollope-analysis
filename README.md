## Trollope Analysis

### Overview 
This is a digital humanities project, designed to help me learn about computational methods for digital history. 

The first sources I'm using are downloaded from Project Gutenberg: works by Anthony Trollope. The 'acquire_gutenberg.ipynb' script might be able to be adapted for other authors but is currently designed for <a href="https://www.gutenberg.org/files/58383/58383-h/58383-h">Trollope's Gutenberg index page</a>. The 'clean_gutenberg.ipynb' might be more broadly useful. The <a href="https://pypi.org/project/gutenberg-cleaner/">gutenberg-cleaner</a> package is used for basic cleaning, with some additional code for content it doesn't catch. A significant amount of additional manual definition of strings is required to produce a clean corpus, added to /modules/text_utils.py. I chose Trollope due to my literary-historical interest in him, but also because of his famously <a href="https://trollopesociety.org/trollope/his-writing/">massive output</a>. 
