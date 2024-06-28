import scribus
import xml.etree.ElementTree as ET

def import_articles_from_xml(xml_file):
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Define initial position for text frames
        x_start = 50
        y_start = 50
        y_offset = 100  # Adjust as needed for spacing between articles

        # Loop through each article
        for idx, article in enumerate(root.findall('article')):
            title = article.find('title').text
            description = article.find('description').text

            # Calculate positions for each article
        x = x_start
        y = y_start + idx * y_offset

        # Create title text frame description text 
        y += 40  # Increase y position for description
        title_frame = scribus.createText(x, y, 400, 30)
        desc_frame = scribus.createText(x, y, 400, 60)

        scribus.setText(title, title_frame)
        scribus.setFont("Arial Bold", title_frame, 1)  # Set font to Arial Bold
        scribus.setFontSize(24, title_frame)  # Set font size to 24 for title
        

        scribus.setText(description, desc_frame)
        scribus.setFont("Arial", desc_frame, 1)  # Set font to Arial
        scribus.setFontSize(12, desc_frame)  # Set font size to 12 for description

       
        # Process each article (e.g., save to CMS, print details, etc.)
        print(f"Title: {title}")
        print(f"Description: {description}")
        print("")

    except IOError:
        print(f"Error: File '{xml_file}' not found or cannot be opened.")
if __name__ == "__main__":
    xml_file = "exmple.xml"  # Replace with your XML file path
    scribus.haveDoc("")
    scribus.messageBox("Error", "No Scribus document open!", scribus.ICON_WARNING, scribus.BUTTON_OK)
    import_articles_from_xml('exmple.xml')