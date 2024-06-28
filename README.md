Scribus XML Article Importer
This script imports articles from an XML file into a Scribus document, creating separate text frames for each article's title and description.

Requirements
Scribus: A free and open-source desktop publishing software. Ensure Scribus is installed on your system.
Scripter Plugin: Enables the execution of Python scripts within Scribus. Ensure it is enabled.
Python: Required to run the script. Python 2.x or 3.x can be used depending on your Scribus version.
XML File: Your articles should be stored in an XML file with the specified format.
Example XML Format
The XML file should be structured as follows save file exmple.xml:

articles>
    <article>
        <title>Breaking News: New Development in Technology</title>
        <description>An exciting breakthrough in technology has been announced, revolutionizing the industry.</description>
    </article>
    <article>
        <title>Market Update: Trends and Analysis</title>
        <description>A comprehensive analysis of current market trends and their implications for businesses.</description>
    </article>
    <article>
        <title>Event Recap: Annual Conference Highlights</title>
        <description>Key highlights and insights from the recent annual conference, showcasing industry leaders and innovations.</description>
    </article>
</articles>

Usage
Open Scribus: Launch Scribus and open an existing document or create a new one.
Run the Script:
In Scribus, go to Script > Execute Script.
Select the import_article.py file and run it.
Handle No Document Warning: If no document is open, the script will display a warning message.
Verify Output: The script reads the articles from the XML file, creates text frames for titles and descriptions, and positions them in the Scribus document.
Script Overview
The script follows these steps:

Parse XML File: Uses Python's xml.etree.ElementTree to parse the XML file.
Iterate Through Articles: Loops through each <article> tag in the XML.
Create Text Frames: For each article, creates a text frame for the title and another for the description.
Set Fonts and Sizes: Sets the font to Arial Bold for titles and Arial for descriptions, with respective font sizes.
Print Article Details: Prints each article's title and description to the console for verification.

