from pdf2image import convert_from_path
import cv2
import numpy as np
import pytesseract


def deskew(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    coords = np.column_stack(np.where(gray > 0))
    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

"""def process_page(page):
    try:
        # Transfer image of pdf_file into array
        page_arr = np.array(page)
        # Transfer into grayscale
        page_arr_gray = cv2.cvtColor(page_arr, cv2.COLOR_BGR2GRAY)
        # Deskew the page
        page_deskew = deskew(page_arr_gray)
        # Cal confidence value
        page_conf = get_conf(page_deskew)
        # Extract string
        d = pytesseract.image_to_data(page_deskew, output_type=pytesseract.Output.DICT)
        d_df = pd.DataFrame.from_dict(d)
        # Get block number
        block_num = int(d_df.loc[d_df['level'] == 2, 'block_num'].max())
        # Drop header and footer by index
        header_index = d_df[d_df['block_num'] == 1].index.values
        footer_index = d_df[d_df['block_num'] == block_num].index.values
        # Combine text in dataframe, excluding header and footer regions
        text = ' '.join(d_df.loc[(d_df['level'] == 5) & (~d_df.index.isin(header_index) & ~d_df.index.isin(footer_index)), 'text'].values)
        return page_conf, text
    except Exception as e:
        # If can't extract then give some notes into df
        if hasattr(e, 'message'):
            return -1, e.message
        else:
            return -1, str(e)
"""

if __name__ == '__main__':

    # Step 1: Reading PDF Files
    pdf_file = 'pdf/P1-10-sequence-learning.pdf'
    pages = convert_from_path(pdf_file)

    # Create a list to store extracted text from all pages
    extracted_text = []

    for page in pages:
        # Step 2: Preprocess the image (deskew)
        preprocessed_image = deskew(np.array(page))

        # Step 3: Extract text using OCR
        text = extract_text_from_image(preprocessed_image)
        extracted_text.append(text)
