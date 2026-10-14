"""English GIMP image editing lesson, three-part task and four activities."""
CONTENT_REVISION = '2026-10-14-dvs24'
LESSON_URL = 'https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81574'
TASK_URL = 'https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81584'
ACTIVITY_URL = 'https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81581'
FILE_ROOT = 'https://learning.noroff.no/pluginfile.php/33156/mod_book/chapter/'
ASSETS = [
 ('Leaves for Question 1',FILE_ROOT+'81584/leaves.jpg'),
 ('Tree for Question 1',FILE_ROOT+'81584/tree.jpg'),
 ('Pineapple for Question 2',FILE_ROOT+'81584/pineapple.jpeg'),
 ('Strawberries for Question 3',FILE_ROOT+'81584/strawberries.jpeg'),
 ('Bananas for flip and rotation activities',FILE_ROOT+'81581/bananas.jpeg'),
 ('Bananas for crop activity',FILE_ROOT+'81581/bananas%20%281%29.jpeg'),
]
FILE_NOTE = 'Open the original Noroff links while signed in. The Question 1 link says tree.png, its URL ends in tree.jpg, and its instruction says tree.jpeg; use the actual linked tree asset and record the downloaded filename. Leaves is labelled leaves.jpeg but its URL ends in leaves.jpg. Renaming a JPEG extension does not convert it to PNG or add transparency. Original course photographs are linked, not republished in Study Buddy.'
CHART_NOTE = 'The supplied Strawberry Sales chart shows Q3 highest, Q2 next, Q1 next and Q4 lowest. The bars share a zero baseline; the axis runs to 40,000 but supplies no unit, year or exact data labels. Describe the ordering without inventing currency, kilograms, causes or exact values. For a precise numeric redesign, obtain the source values and unit rather than measuring or guessing bar endpoints. Question 3 asks for an image illustrating the chart and allows your own composition; an exact chart remake is not specified.'
MANUAL_LINKS = [
 ('Desaturate','https://docs.gimp.org/3.0/en/gimp-filter-desaturate.html'),
 ('Image transforms','https://docs.gimp.org/3.0/en/gimp-image-transform.html'),
 ('Flip tool','https://docs.gimp.org/3.0/en/gimp-tool-flip.html'),
 ('Fuzzy Select','https://docs.gimp.org/3.0/en/gimp-tool-fuzzy-select.html'),
 ('Layer masks','https://docs.gimp.org/3.0/en/gimp-layer-mask-add.html'),
 ('Layers and opacity','https://docs.gimp.org/3.0/en/gimp-dialogs-structure.html'),
 ('Color to Alpha','https://docs.gimp.org/3.0/en/gimp-filter-color-to-alpha.html'),
 ('Pattern fill','https://docs.gimp.org/3.0/en/gimp-edit-fill-pattern.html'),
 ('Alpha to Selection','https://docs.gimp.org/3.0/en/gimp-layer-alpha-selection-replace.html'),
 ('Save and Export','https://docs.gimp.org/3.0/en/gimp-images-out.html'),
]
TASK_STEPS = [
 ('1. Plan the three designs and get source files','Open the original Task 2.4. Download the linked leaves, tree, pineapple and strawberries images while signed in. Keep originals and work in separate projects for Questions 1–3. Record actual filenames and your GIMP version.','The brief specifies three image-editing outputs, no font/page count or mandatory export format. XCF projects, exports and notes below are recommended study evidence.'),
 ('2. Question 1 — isolate the tree','Open leaves as the base image, then File → Open as Layers to add the linked tree. Name both layers. Select the tree, select its background with Fuzzy Select if suitable, then invert the selection to retain the tree. Add a layer mask initialised from Selection. Clear the selection and refine the mask at branches and edges.','If similar colours remove branches, adjust the selection or paint the mask. White reveals, black hides, grey partly reveals. Click the mask thumbnail before editing it; keep original pixels available.'),
 ('3. Question 1 — set leaves opacity to 80','Keep the isolated tree above leaves. Select the LEAVES layer and set its layer opacity to 80%. Move/scale the correct tree layer as needed and review the combined image. An optional backing layer below leaves can make the semi-transparent base easier to view.','80 applies to leaves, not tree: the lesson butterfly example used a different 60% value. Opacity affects a whole layer; a mask controls individual locations. Record actual layer order and any optional backing.'),
 ('4. Question 2 — isolate the pineapple','Start a separate project from pineapple.jpeg. Preserve an original copy. Select the pineapple including its crown, or select background and invert, then create a Selection layer mask. Refine edges against light and dark temporary backing colours.','A checkerboard indicates transparency; it is not the requested final background. Fuzzy Select follows connected similar colours and can miss separate background regions.'),
 ('5. Question 2 — add the Stone pattern','Create a new full-canvas layer below the pineapple cutout. Clear the selection so it does not restrict the fill. Find the Stone pattern in the Patterns dialog, select it, select the background layer and use Edit → Fill with Pattern. Check layer visibility and order.','Use Stone as requested. If your installation lacks it, record the missing pattern and seek a tutor-approved source or equivalent; do not silently substitute or claim a check was completed.'),
 ('6. Question 3 — illustrate strawberry sales','Read the supplied chart, then use the linked strawberries.jpeg in an original composition. One optional design is the strawberry image beside a short text summary: Q3 highest, Q2 next, Q1 next, Q4 lowest. Use readable quarter labels and maintain the chart’s meaning.','No exact values, unit or year are supplied in labels. Do not invent them or suggest seasonal causes. A decorative strawberry photo is not automatically a quantitative chart; if you add one, use verified data and honest encodings.'),
 ('7. Save, export and review all three outputs','Save each editable project as XCF and export a sharing image, for example PNG. Reopen your exports to inspect cutout edges, Stone background, readable labels and the intended composition. Record project/export paths and actual checks, then transfer written notes and the selected step to Exam Resolver.','These file/log suggestions are study scaffolds, not additional brief requirements. XCF keeps layers/masks but not undo history. JPEG has no alpha transparency. Resolver reviews written notes; it does not inspect image pixels or operate GIMP.'),
]
TASK_TEMPLATE = '''# Task 2.4 Three image designs

## Source and setup record
GIMP version and platform: [...]
Actual downloaded filenames and original task URL: [...]

## Question 1 Leaves and tree
Tree background removal method and mask refinement: [...]
Actual layer order: [...]
Leaves layer opacity setting and evidence: [80% after checking]
Optional backing or layout changes and reason: [...]
XCF project and exported image paths: [...]
Checks actually performed and issues still to fix: [...]

## Question 2 Pineapple and Stone
Selection/mask method and crown/edge checks: [...]
Stone pattern availability and actual name: [...]
Background layer below the pineapple and fill scope: [...]
XCF project and exported image paths: [...]
Checks actually performed and issues still to fix: [...]

## Question 3 Strawberry sales illustration
How I used the supplied strawberries image: [...]
My composition and reason: [...]
How it communicates Q3 > Q2 > Q1 > Q4: [...]
Exact values/unit/year source if added: [not supplied by chart labels]
XCF project and exported image paths: [...]
Readability and meaning checks actually performed: [...]

## Final review
Original photographs retained: [...]
All three images created and reopened: [complete after checking]
Unfinished work, placeholders and tutor questions: [...]

The brief specifies image designs, no font/page count or export format. This optional worksheet does not replace the images and does not claim that GIMP operations or image checks have happened.
'''
EVIDENCE_TEMPLATE = '''# Lesson 2.4 Editing and export log

Repeat this record for each project or self-study activity.
Project and task/activity number: [...]
Original file and source: [...]
Selected layer or mask thumbnail: [...]
Operation, settings and intended result: [...]
What I actually observed: [...]
Correction made or next check planned: [...]
Editable XCF path: [...]
Export path, format and settings: [...]
Actual reopen result: [...]

Separate planned actions from completed checks. A screenshot of layer settings may support your notes, but Exam Resolver does not inspect image pixels. Do not describe an illustration in Study Buddy as your own completed GIMP project.
'''
ACTIVITY_DATA = [
 ('2.4.1','Flip the bananas vertically',[
  ('Open a fresh copy','Open the linked bananas image and preserve the original. Work from the original separately from the rotation exercise.','The request says flip upside down; this guide interprets it as a vertical mirror, distinct from the separate 180-degree rotation activity.'),
  ('Apply a vertical flip','Use Image → Transform → Flip Vertically for the whole image, or the Flip tool with the intended layer target and Vertical direction.','Choose direction in Tool Options. The manual documents Ctrl to toggle directions; right-click is not the documented vertical-flip shortcut.'),
  ('Compare and record','Compare top/bottom and left/right positions with the original, then save/export a separate result and record actual checks.','A vertical flip swaps top and bottom without reversing left/right positions. It is not a 180-degree rotation.')]),
 ('2.4.2','Crop the bananas to the centre',[
  ('Choose the centre','Open the crop activity’s banana link. Use Rectangle Select to mark the central area you want to keep.','The brief gives no exact crop dimensions; record your chosen rectangle.'),
  ('Crop the image','Use Image → Crop to Selection. Check that the side regions are removed and the intended central content remains.','Cropping removes outer content; it is not resizing the whole image.'),
  ('Save and review','Save/export separately and reopen to check the crop. Record the before/after pixel dimensions if useful.','Do not overwrite your source or reuse this cropped result as the starting point for the independent rotation exercise.')]),
 ('2.4.3','Rotate the bananas 180 degrees',[
  ('Open the original','Open a fresh original banana image rather than the already flipped or cropped result.','Keep the activities independent so you can explain each operation.'),
  ('Rotate 180 degrees','Use Image → Transform → Rotate 180° for the whole image. If using the Rotate tool, choose the correct target and enter 180°.','Rotation turns the image; it reverses both top/bottom and left/right positions, unlike a vertical mirror.'),
  ('Save and compare','Save/export a separate result and compare recognisable details with the original. Record actual checks.','Do not claim a rotation based only on an unchanged layer name.')]),
 ('2.4.4','Fill Data Analyst text with a pattern',[
  ('Create editable text','Create a new project and use the Text tool to type exactly Data Analyst. Keep this editable text layer.','Font, canvas size and specific pattern are your choices; maple leaves is an example.'),
  ('Select the letter shapes','Select only the text layer, then Layer → Transparency → Alpha to Selection. Create a separate transparent pattern layer above it and keep the letter selection active.','Filling the pattern layer changes pixels there, not the editable original text. Multiple selected layers can change the alpha selection.'),
  ('Fill the selection','Choose a pattern in the Patterns dialog and use Edit → Fill with Pattern on the new pattern layer. Clear the selection and inspect letter edges.','An empty selection fills the entire layer; keep the letter selection active for this activity.'),
  ('Review text and export','Save the layered project and export a sharing image. Reopen and check that Data Analyst remains readable and the pattern is inside the letters.','If the text changes, recreate the alpha selection and pattern fill; the raster pattern layer does not automatically track later text edits.')]),
]
GUIDE = {'course_code':'FI1BBDV75','id':'2.4-task','uid':'dvs-2.4-task-81584','lesson_number':'2.4','title':'Three image designs with GIMP','source_url':TASK_URL,'method':'image_manipulation','deliverable':'Question 1: blend leaves and isolated tree with leaves opacity 80%. Question 2: pineapple on a Stone pattern background. Question 3: an original strawberry image illustrating the supplied sales chart.','steps':[s[1] for s in TASK_STEPS],'caution':'Use the actual linked source images. File labels differ for the tree. Do not invent chart units/values or completed image checks. No font/page count or export format is specified; templates are optional study scaffolds.','task_dataset':'','template_file':'DVS Task 2.4 GIMP Image Design Worksheet.docx'}
GUIDES = [GUIDE]
ACTIVITY_STEPS = {}
ACTIVITY_TEMPLATES = {}
for number,title,steps in ACTIVITY_DATA:
    uid=f'dvs-{number}-activity-81581'
    guide={'course_code':'FI1BBDV75','id':number,'uid':uid,'lesson_number':'2.4','title':title,'source_url':ACTIVITY_URL,'method':'image_manipulation_activity','deliverable':title+'. Save/export separately and record your actual checks as optional study evidence.','steps':[s[1] for s in steps],'caution':steps[-1][2]+' Do not invent completed GIMP actions or observations.','task_dataset':'','template_file':''}
    GUIDES.append(guide);ACTIVITY_STEPS[number]=steps
    ACTIVITY_TEMPLATES[uid]=f'# Activity {number} {title}\n\nSource file and GIMP version: [...]\nSelected target and operation/settings: [...]\nMy actual result and explanation: [...]\nEditable project and export paths: [...]\nActual reopen check or remaining issue: [...]\n\n'+guide['caution']+'\n'

VERSION_NOTES = '''### Menu and version notes

The course includes older GIMP screenshots. The linked official **3.0 manual** was checked on 14 October 2026; your installed version may differ. Use command names and inspect Tool Options rather than memorising screenshots.

- **Colors → Desaturate → Desaturate** changes an RGB layer to shades of grey; it is not a two-colour black/white threshold. Course brightness −40 and contrast 25 are practice settings, not universally suitable values.
- **Colors → Color to Alpha** is the documented menu location. It can affect matching colours inside the subject as well as the background. Preview and inspect edges; selection/masking often gives more control.
- **Flip direction** is selected in Tool Options; Ctrl can toggle it. The course’s left/right-click claim is not the documented method.
- **Copy then Edit → Paste as → Paste as Single Layer** explicitly creates a new layer. Paste behaviour varies; do not assume every Ctrl+V result is already an independent layer.
- **Layer opacity** and **layer masks** are different controls. For Task 2.4 Question 1, select leaves and set 80%; the butterfly lesson example’s 60% is not the task setting.
- **Save XCF** for editable layers/masks; **Export** a sharing format. Keep separate originals and reopened exports. A supplied photo can be illustration context without becoming proof of numeric values.
'''
SOURCES = '\n\n'.join(f'[{title}]({url}).' for title,url in MANUAL_LINKS)

def get_task_guide_markdown(guide=None):
    guide=GUIDE if guide is None else guide
    steps=TASK_STEPS if guide['id']=='2.4-task' else ACTIVITY_STEPS[guide['id']]
    prefix='Task' if guide['id']=='2.4-task' else 'Activity'
    text=f"### DVS {prefix} {guide['id'].replace('-task','')}: {guide['title']}\n\n**Deliverable:** {guide['deliverable']}\n\n"
    for title,instruction,caution in steps:text+=f'#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n'
    if guide['id']=='2.4-task':text+='\n'+FILE_NOTE+'\n\n'+CHART_NOTE+'\n\n'+VERSION_NOTES
    files = ASSETS[:4] if guide['id']=='2.4-task' else ([ASSETS[5]] if guide['id']=='2.4.2' else ([] if guide['id']=='2.4.4' else [ASSETS[4]]))
    text+='\n\n### Original source files\n\n'+('\n'.join(f'- [{name}]({url})' for name,url in files) if files else 'Create a new project and the text Data Analyst; no supplied photograph is required.')+'\n\n'
    text+=f"[Original brief]({guide['source_url']}).\n\n### Official GIMP references\n\n"+SOURCES
    text+='\n\nExam Resolver reviews supplied written notes and source descriptions. It does not inspect image pixels, open XCF projects, run GIMP, verify layer settings or submit work. Record only checks you actually performed. Original compositions are individual; this is a study guide, not a completed official solution.'
    return text

ILLUSTRATIONS = [
 {'file':'lesson-2-4-transforms.png','title':'Transform with intention','caption':'Flip mirrors, rotation turns, crop removes outer content, scale resamples and shear slants. A vertical mirror and a 180-degree rotation have different effects. These conceptual examples are not actual GIMP screenshots or completed activity outputs.'},
 {'file':'lesson-2-4-layers-masks.png','title':'Build images with layers and masks','caption':'Mask the tree above leaves; Question 1 sets the leaves layer opacity to 80%. For Question 2, keep the pineapple cutout above the Stone pattern. White reveals, black hides and grey partly reveals on a mask. A checkerboard is only a transparency indicator. Illustrative scenes are not the original course photographs.'},
 {'file':'task-2-4-three-designs.png','title':'Plan the three image designs','caption':'Blend leaves/tree, replace the pineapple background with Stone, and use the supplied strawberries image to illustrate Q3 highest, Q2 next, Q1 next, Q4 lowest. The concept sketch gives no exact values or invented unit. Your own composition is allowed; generated examples do not satisfy the task for you.'},
]
LESSON_CONTENT = '''
### Lesson 2.4: edit images with a clear purpose

Use GIMP to change a photo’s tone or framing, separate a subject from its background and compose several images. Begin by identifying the intended output and preserving the original. The three-part task asks for your own image designs; written explanations and the templates support that work.

### Step 1 — prepare an editable workflow

Open an image with File → Open; add another to the same project with File → Open as Layers. Rename layers by their role and select the intended layer before editing. Keep an original copy and save an XCF project. GIMP is primarily a raster editor even though paths can help create selections; paths do not make the whole photo a vector image. Avoid relying on the lesson’s old version numbers or unsupported popularity/history claims.

### Step 2 — convert colour to shades of grey

Select an RGB layer and use Colors → Desaturate → Desaturate. Preview a mode and compare important details before accepting. The result normally contains many grey levels; a binary threshold is a different operation. Brightness and contrast can help tonal separation but can also lose highlights or shadows. The course example uses brightness −40 and contrast 25 on birds; those settings are optional practice, not Task 2.4 requirements. [Official desaturation reference](https://docs.gimp.org/3.0/en/gimp-filter-desaturate.html).

### Step 3 — distinguish transforms

A vertical flip mirrors top and bottom; a 180° rotation turns both vertical and horizontal positions. Crop keeps a selected region and removes outer content. Scale changes pixel dimensions through resampling; preserve aspect ratio unless distortion is intended. Shear slants the geometry. Use the whole-image commands under Image → Transform when changing the entire photo, and the appropriate layer target for component edits. Image → Crop to Selection crops a marked central region. [Image transforms](https://docs.gimp.org/3.0/en/gimp-image-transform.html). [Flip tool and direction](https://docs.gimp.org/3.0/en/gimp-tool-flip.html).

### Step 4 — select a subject and refine a mask

Fuzzy Select finds connected regions with similar colours; it is not an automatic object recogniser. Adjust the threshold and selection if background islands or subject details are missed. If you selected the background, invert before creating a Selection layer mask to retain the subject. Clear the selection afterwards, then edit the mask thumbnail: white reveals, black hides and grey allows partial visibility. Inspect fine edges with contrasting backing colours. Keep pixels and masks separate so you can revise the cutout. [Fuzzy Select](https://docs.gimp.org/3.0/en/gimp-tool-fuzzy-select.html). [Add Layer Masks](https://docs.gimp.org/3.0/en/gimp-layer-mask-add.html).

### Step 5 — compose with layers and patterns

Put the cutout above the replacement background. Layer opacity changes the entire selected layer; a mask controls visibility at each location. Move or scale the intended layer, checking boundaries and composition. For a full-canvas pattern background, clear any selection, create/select a background layer and use Edit → Fill with Pattern with the chosen pattern. For patterned letters, keep the letter selection active so only those shapes are filled on a separate layer. [Layers and opacity](https://docs.gimp.org/3.0/en/gimp-dialogs-structure.html). [Pattern fill](https://docs.gimp.org/3.0/en/gimp-edit-fill-pattern.html).

### Step 6 — complete the task and independent activities

**Question 1:** open leaves, add the linked tree as a layer, remove its background and set **leaves opacity to 80%**. Keep the tree above leaves; the butterfly demonstration’s 60% is a different example.

**Question 2:** remove the pineapple background and add the **Stone** pattern below it. If Stone is missing in your version, document it and ask the tutor for an approved source or equivalent.

**Question 3:** use the linked strawberries photo to make your own image illustrating the supplied chart. Communicate its meaning without inventing values or units. The brief gives freedom over the composition.

**Separate self-study activities:** 2.4.1 vertically flips bananas, 2.4.2 crops the centre, 2.4.3 rotates a fresh original 180°, and 2.4.4 fills the words **Data Analyst** with a chosen pattern. Keep these distinct from the three task questions. The walkthrough video was not played; try the operations yourself first.

'''+FILE_NOTE+'\n\n'+CHART_NOTE+'\n\n'+VERSION_NOTES+'''
### Step 7 — save, export and explain your choices

Save editable XCF projects and export suitable sharing images; these are recommended study practices, not a specified submission format. Reopen exports to inspect edges, layer visibility, text legibility and intended meaning. Keep recorded observations separate from planned checks. The brief supplies no page count or font and does not require a written report instead of the images.

Use the task or activity worksheet to record actual actions, then Prepare in Exam Resolver to transfer your notes and selected step. The resolver reviews text and supplied descriptions, not image pixels or live GIMP projects. It cannot verify that a layer is 80% opaque or that a file reopens correctly for you.

[Original lesson](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81574). [Black and white](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=123257). [Transforms](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=123258). [Backgrounds](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=123260). [Blending](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=123261). [Other functions](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=123262). [Self-study](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81581). [Task](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81584).
'''

def get_lesson():
    return {'course_code':'FI1BBDV75','lesson_number':'2.4','title':'Basics of Image Manipulation with GIMP','module_number':2,'module_title':'User Experience and User Experience Design','source_url':LESSON_URL,'source_checked_on':'2026-10-14','content':LESSON_CONTENT.strip(),'illustration':None,'dvs_illustrations':ILLUSTRATIONS,'key_points':['Select the intended layer or mask before editing','Flip, rotation, crop and scale have different effects','Question 1 changes leaves opacity to 80%; Question 2 uses Stone','Use strawberries to illustrate the chart without inventing data','Save editable projects and record actual export checks'],'visual_elements':{'diagrams':False,'tables':False,'highlighted_sections':True}}
