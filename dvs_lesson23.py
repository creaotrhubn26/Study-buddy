"""English graphics/GIMP lesson and seven-question Task 2.3 study workflow."""
CONTENT_REVISION = '2026-10-14-dvs23'
LESSON_URL = 'https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81563'
TASK_URL = 'https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81573'
COREL_URL = 'https://www.coreldraw.com/en/product/family/'
PROCREATE_URL = 'https://apps.apple.com/no/app/procreate/id425073498'
PHOTOPEA_URL = 'https://www.photopea.com/'
PHOTOPEA_LEARN_URL = 'https://www.photopea.com/learn/'
GIMP_URL = 'https://www.gimp.org/downloads/'
GIMP_SAVE_URL = 'https://docs.gimp.org/3.0/en/gimp-images-out.html'
PRICE_NOTE = 'Research snapshot: 14 October 2026. Prices depend on edition, storefront, currency, tax and payment period. CorelDRAW Graphics Suite’s public page displayed NOK 4,240/year including VAT; Procreate’s Norwegian App Store listing displayed NOK 179 as an app purchase; Photopea’s Account panel displayed a free plan at EUR 0/month and a prepaid Premium example of EUR 15 for 90 days, described as EUR 5/month, with one-time payments rather than an automatic subscription. These are dated public examples, not a business quote or directly comparable lifetime costs. Recheck official sources for your own report.'
PRODUCTS = [
 {'name':'CorelDRAW Graphics Suite','platform':'Windows and macOS desktop; subscriber browser offering. Other CorelDRAW editions differ.','price':'Public example: NOK 4,240/year including VAT. Subscription and one-time purchase options exist; verify the edition and business licence.','graphics':'CorelDRAW supplies vector illustration/page layout; the Suite includes PHOTO-PAINT for raster editing.','functions':'Examples to investigate: multi-page layout, typography, bitmap-to-vector tracing and colour-managed print output.','source':COREL_URL,'limit':'Do not attribute every Suite feature or platform to Standard or Go; validate company requirements.'},
 {'name':'Procreate','platform':'iPad app; check supported iPad and iPadOS versions. Procreate Pocket is a separate iPhone product.','price':'Norwegian App Store example: NOK 179 app purchase. Include device/stylus costs if relevant to the case.','graphics':'Primarily raster drawing/painting; vector text does not make it a general vector-layout editor.','functions':'Examples: custom brushes, layers and masks, adjustments and frame-by-frame animation.','source':PROCREATE_URL,'limit':'A low app price does not establish suitability for a desktop office or multi-page print workflow.'},
 {'name':'Photopea','platform':'Browser-based editor on compatible devices; evaluate screen size, input and performance for the actual workflow.','price':'Free ad-supported plan; Account displayed prepaid Premium EUR 15/90 days (EUR 5/month equivalent), not an automatic recurring subscription.','graphics':'Supports raster and vector graphics; examine its specific vector and export capabilities.','functions':'Examples: layers, masks, smart objects, adjustment tools and paths.','source':PHOTOPEA_URL,'limit':'Record the exact Account offer and terms. Do not assume every browser/device or imported format behaves identically.'},
]
TASK_STEPS = [
 ('1. Identify the two graphics types','Question 1 asks for two types. Distinguish raster images built from pixels from vector graphics described through shapes and paths. Explain how each stores the image and behaves when scaled.','Study focus: raster and vector. File extensions alone do not prove that a document contains only one kind of content.'),
 ('2. Recognise five raster formats','Question 2 asks for five raster formats from the supplied choices. Use PNG, JPEG, GIF, TIFF and BMP as the course examples and explain an appropriate use or limitation.','JPEG does not support alpha transparency. Raster formats can use different colour modes, bit depths and compression; not every image is 24-bit RGB.'),
 ('3. Recognise three vector formats','Question 3 asks for three vector formats. Use SVG, EPS and PS as the course examples and explain the role of geometry, paths and scaling.','SVG, EPS and PS can also contain embedded raster content. A rasterised export is pixel-based even if it began with vector shapes.'),
 ('4. Explain pixel storage','Question 4 asks which type records individual pixels: raster. For an 8-bit-per-channel RGB example, explain three channels, 256 levels per channel and 24 bits per pixel. Alpha is a separate opacity channel.','800×600 pixels = 480,000 pixels; RGB payload = 1,440,000 bytes, RGBA = 1,920,000 bytes at 8 bits per channel. These are raw payloads, not guaranteed compressed file sizes.'),
 ('5. Match three raster editing tools','Question 5 asks for three raster-oriented choices from its list. The course groups GIMP, Canva and Adobe Photoshop here. Explain their primary role for the question and the difference between pixel editing and template-based design.','Do not claim tools have no capabilities outside their primary category. Current features, licences and prices need checking rather than repeating old course prices.'),
 ('6. Match two vector editing tools','Question 6 asks for two vector-oriented choices from its list. The course examples are Inkscape and Adobe Illustrator. Explain why paths and object editing suit scalable diagrams or logos.','Importing a bitmap or supporting text/paths does not make a product equivalent to a dedicated vector editor. Validate the required output format.'),
 ('7. Compare the three software candidates','Question 7 concerns a hypothetical ordinary paper company with year-end funds remaining. Research CorelDRAW, Procreate and Photopea. Include at least supported platforms, price, raster/vector support and complex functions. Specify the CorelDRAW edition, cite official evidence with dates, and explain the differences.','Company devices, budget and exact artwork needs are not supplied. Label assumptions and unknowns; a recommendation is optional. Compare currency, tax and licence duration fairly. The task states no page count or font requirement.'),
]
STUDY_TEMPLATE = '''# Task 2.3 Questions 1–6 — Study answers

## Question 1: Graphics types (two)
My choices: [...]
How storage and scaling differ: [...]

## Question 2: Raster formats (five)
My choices: [...]
Use or limitation for each: [...]

## Question 3: Vector formats (three)
My choices: [...]
Geometry and embedded raster caveat: [...]

## Question 4: Individual pixel information
My choice and reason: [...]
Optional RGB/RGBA raw-payload calculation with assumptions: [...]

## Question 5: Raster editing software (three)
My choices: [...]
Primary roles and current-feature caveats: [...]

## Question 6: Vector editing software (two)
My choices: [...]
Why object/path editing fits a scalable graphic: [...]

## Review
Explain the concepts in your own words. Record errors or questions to revisit. This is a study worksheet, not an automatic Noroff quiz submission.
'''
COMPARISON_TEMPLATE = '''# Task 2.3 Question 7 — Software comparison

## Case scope
Supplied context: hypothetical ordinary paper company; year-end funds remain; candidates are CorelDRAW, Procreate and Photopea.
Device fleet, budget and graphics needs to confirm: [...]
Clearly labelled assumptions: [...]
Comparison date and intended audience: [...]

'''
for name in ['CorelDRAW (specify edition)','Procreate','Photopea']:
    COMPARISON_TEMPLATE += f'## {name}\nSupported platforms and requirements: [...]\nPrice, currency, tax, licence/payment period: [...]\nRaster/vector capabilities and limits: [...]\nComplex functions relevant to the company: [...]\nOfficial sources, access date and unresolved points: [...]\n\n'
COMPARISON_TEMPLATE += '''## Explain the main differences
Platform fit: [...]
Cost model and fair comparison period: [...]
Graphics/output fit and complex functions: [...]
Limits and information to confirm: [...]
Optional conditional recommendation and reasons: [...]

## Final review
Cover all three candidates and all four required dimensions. Cite dated primary evidence, distinguish editions and separate checked claims from assumptions. Do not silently convert currencies or treat annual and one-time prices as equivalent. The brief states no page count or font requirement.
'''
SETUP_TEMPLATE = '''# Lesson 2.3 Optional GIMP orientation log

## Setup record
Official download source: https://www.gimp.org/downloads/
Platform and architecture: [...]
Version actually installed: [complete after installation]
Date: [...]

## Find the five workspace areas
Image window and top menu: [...]
Toolbox: [...]
Tool options: [...]
Brushes, patterns and gradients: [...]
Layers: [...]

## Small practice project
Original image and permission/source: [...]
Layer selected and simple change: [...]
Editable XCF project path: [...]
Exported PNG/JPEG path and settings: [...]
Actual reopen/check result: [complete only after checking]

Save an editable XCF project; export a sharing image. XCF does not preserve undo history. JPEG has no alpha transparency. An SVG opened as an image in GIMP is rasterised at an import size. Interface details vary by version. This log is optional lesson practice, not an extra Task 2.3 requirement.
'''
RESEARCH_NOTES = '### Dated software research examples\n\n'+PRICE_NOTE+'\n\n'
for p in PRODUCTS:
    RESEARCH_NOTES += f"**{p['name']}**\n\n- **Platforms:** {p['platform']}\n- **Price/licence:** {p['price']}\n- **Graphics:** {p['graphics']}\n- **Complex functions:** {p['functions']}\n- **Check:** {p['limit']}\n\n[Official source]({p['source']}).\n\n"
RESEARCH_NOTES += '[Photopea capability documentation]('+PHOTOPEA_LEARN_URL+'). Recheck evidence before completing your own comparison. These records are research starting points, not a completed company assessment.\n'
COMPARISON_EXAMPLE = """### Question 7 example reasoning to adapt

The main differences are platform support, payment model and intended workflow. CorelDRAW Graphics Suite combines vector design and page layout with raster editing through PHOTO-PAINT. Procreate focuses on raster drawing and painting on an iPad. Photopea supports raster and vector editing in a browser with a free option.

For the hypothetical paper company, first confirm devices and graphics requirements. If it needs only occasional image editing, Photopea could be a starting point. More demanding layout and print work could justify CorelDRAW, while Procreate could fit employees who already use iPads for illustration. These are conditional judgements, not findings about the company's actual needs. Add your dated price records, required platform details, complex functions and source links to complete the comparison.
"""
ILLUSTRATIONS = [
 {'file':'lesson-2-3-raster-vector.png','title':'Raster pixels and vector paths','caption':'Raster images store pixels; vector graphics describe geometry. Choose a format for the content and output. Vector documents may include raster images, and rasterised exports still have pixels. The poster itself is a raster PNG illustration of both concepts, not a scalable vector asset.'},
 {'file':'lesson-2-3-gimp-workspace.png','title':'Find your way around GIMP','caption':'Locate the image window/menu, toolbox, tool options, brushes/patterns/gradients and layers. Save the editable project as XCF and export an image for sharing. XCF does not preserve undo history; JPEG has no alpha transparency. This conceptual workspace is not an actual GIMP screenshot; layout and menu details vary by version.'},
 {'file':'task-2-3-software-comparison.png','title':'From concepts to software comparison','caption':'Questions 1–6 check graphics types, file formats, pixel storage and editing-tool roles. Question 7 researches CorelDRAW, Procreate and Photopea for a hypothetical paper company, covering platforms, price/licence, raster/vector support and complex functions. Specify editions and dated official evidence; do not invent company needs or a winning product.'},
]
LESSON_CONTENT = '''
### Lesson 2.3: graphics, formats and GIMP

Computer graphics covers creating, displaying and editing visual content, including photographs, diagrams, illustrations and interfaces. This lesson connects how an image is represented to the editor and output you choose.

### Step 1 — distinguish raster and vector

**Raster:** an image is a grid of pixels. It suits photographs, textures and direct pixel editing. Enlarging a limited-resolution raster requires resampling; interpolation cannot recover original detail that was not recorded. Shrinking, enlarging and changing the displayed size have different effects.

**Vector:** objects are described with geometry such as points, curves and shapes. This suits scalable diagrams, lettering and logos. Geometry can be redrawn at another size, but embedded raster images still have resolution limits. Complex vectors are not necessarily smaller files, and rasterising a vector creates a pixel image.

### Step 2 — connect formats to purpose

Course raster examples: **PNG, JPEG, GIF, TIFF and BMP**. JPEG commonly uses lossy compression and has no alpha channel. PNG supports lossless compression and transparency in suitable colour modes. File size depends on dimensions, colour mode, bit depth, compression and content.

Course vector examples: **SVG, EPS and PS**. They can contain vector descriptions and can also include raster content. SVG is widely supported on the web, but fonts, embedded content and application features can affect portability. Preserve editable originals and inspect the final export.

### Step 3 — understand RGB and alpha

In an **8-bit-per-channel RGB example**, each channel has 256 levels (0–255), giving 24 bits or 3 bytes per pixel and 16,777,216 possible RGB combinations. RGB is additive: red plus green produces yellow; black is (0,0,0), white is (255,255,255). These assumptions do not describe every raster format or colour mode.

An 8-bit alpha channel records 256 opacity levels. It affects how the RGB colour is composited; it does not add new opaque RGB colours. At 8 bits per channel, RGBA uses 32 bits or 4 bytes per pixel.

For 800×600: 480,000 pixels × 3 bytes = **1,440,000 bytes** of raw RGB payload, or × 4 = **1,920,000 bytes** for RGBA. Headers, compression and other data change the actual file size. Changing print-resolution metadata alone does not create more pixels.

### Step 4 — choose software for the job

The course uses **GIMP, Canva and Photoshop** as raster-oriented examples, and **Inkscape and Illustrator** as vector-oriented examples. These are primary-role categories for the activity, not claims that each product has only one capability. Canva is a template/design platform rather than a direct equivalent of a pixel editor.

Consider output, device support, training, interoperability, licence terms and the functions actually needed. A paid licence does not guarantee a particular support response time, and a free editor is not automatically unsuitable for professional work. Recheck current product details rather than repeating the course’s historical price examples.

### Step 5 — orient yourself in GIMP

Use the [official download page](https://www.gimp.org/downloads/) and select your operating system and architecture. On 14 October 2026 it listed stable **GIMP 3.2.6**, released 10 September 2026. Record the version you actually use; course screenshots and the linked 3.0 manual may differ from your installation.

Find five areas: **image window and top menu; toolbox; tool options; brushes/patterns/gradients; layers**. Select the intended layer before editing. Tool options change with the selected tool. Menu groups include File, Edit, Select, View, Image, Layer, Colors, Tools, Filters, Windows and Help. [GIMP workspace documentation](https://docs.gimp.org/3.0/en/gimp-concepts-main-windows.html).

**Save** an editable **XCF** project. **Export** a sharing format such as PNG or JPEG, with appropriate settings. XCF retains project structure but not undo history; an exported flat image is not a substitute for the editable project. [GIMP Save/Export documentation](https://docs.gimp.org/3.0/en/gimp-images-out.html).

The optional orientation log below records real setup and reopen checks. It is lesson practice, not an extra official task deliverable.

### Step 6 — work through the seven-question task

The Noroff task is an embedded **H5P activity with seven questions**. Questions 1–6 ask for the graphics types, five raster formats, three vector formats, pixel-based representation, three raster-oriented tools and two vector-oriented tools. Use the step selector to explain your reasoning and record study answers.

**Question 7:** a hypothetical ordinary paper company has funds remaining near year end. Compare **CorelDRAW, Procreate and Photopea**, including at least **platforms, price, raster/vector support and complex functions**. Record primary sources and dates, specify editions and payment periods, and explain relevant differences. Devices, budget and precise needs are not supplied: keep assumptions explicit. A recommendation is optional; the brief specifies no page count or font.

'''+RESEARCH_NOTES+'\n'+COMPARISON_EXAMPLE+'''
### Step 7 — prepare a review in Exam Resolver

Use the study worksheet and comparison template, then transfer your written notes and selected question step. The resolver reviews supplied text and dated evidence; it does not submit or grade the H5P activity, install GIMP, inspect project/image pixels or check current prices live. Review placeholders and recheck product evidence before finalising Question 7.

[Original lesson](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81563). [Raster explanation](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81566). [Vector explanation](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81567). [GIMP installation](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=123242). [GIMP overview](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=123255). [Original seven-question task](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81573).
'''
GUIDE = {'course_code':'FI1BBDV75','id':'2.3-task','uid':'dvs-2.3-task-81573','lesson_number':'2.3','title':'Graphics study questions and software comparison','source_url':TASK_URL,'method':'graphics_comparison','deliverable':'Study answers for seven H5P questions. Question 7 compares CorelDRAW, Procreate and Photopea: platforms, price, raster/vector support and complex functions.','steps':[s[1] for s in TASK_STEPS],'caution':'No automatic quiz submission or grading. Label company assumptions, specify product editions and dated evidence, and recheck prices. No page count or font is specified.','task_dataset':'','template_file':'DVS Task 2.3 Graphics Questions and Software Comparison.docx'}

def get_task_guide_markdown(guide=None):
    text='### DVS Task 2.3: Graphics study questions and software comparison\n\n**Deliverable:** '+GUIDE['deliverable']+'\n\n'
    for title,instruction,caution in TASK_STEPS:
        text+=f'#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n'
    text+='\n'+RESEARCH_NOTES+'\n'+COMPARISON_EXAMPLE
    text+=f'[Original embedded task]({TASK_URL}). [GIMP download]({GIMP_URL}). [GIMP Save/Export]({GIMP_SAVE_URL}).\n\nUse your own explanation and cite dated primary evidence. Templates are optional study scaffolds. Exam Resolver reviews supplied written notes; it does not submit or grade H5P answers, install software, inspect project pixels or check live prices. This guide is not an official completed solution.'
    return text

def get_lesson():
    return {'course_code':'FI1BBDV75','lesson_number':'2.3','title':'Introduction to Graphics and GIMP','module_number':2,'module_title':'User Experience and User Experience Design','source_url':LESSON_URL,'source_checked_on':'2026-10-14','content':LESSON_CONTENT.strip(),'illustration':None,'dvs_illustrations':ILLUSTRATIONS,'key_points':['Raster stores pixels; vector describes geometry and may embed pixels','RGB/RGBA memory examples need explicit bit-depth assumptions','Save editable XCF and export the sharing image','Seven-question task ends with a dated three-product comparison'],'visual_elements':{'diagrams':False,'tables':False,'highlighted_sections':True}}
