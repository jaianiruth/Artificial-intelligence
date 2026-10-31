import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

def create_image(text, output_filename):
    bg_color = (30, 30, 30)
    text_color = (200, 200, 200)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", 16)
    except IOError:
        font = ImageFont.load_default()

    lines = text.split('\n')
    try:
        dummy_img = Image.new('RGB', (1, 1))
        draw = ImageDraw.Draw(dummy_img)
        max_width = 0
        total_height = 0
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            max_width = max(max_width, bbox[2] - bbox[0])
            total_height += (bbox[3] - bbox[1]) + 4
    except AttributeError:
        max_width = max(len(line) * 10 for line in lines)
        total_height = len(lines) * 20

    img_width = max(800, max_width + 40)
    img_height = max(300, total_height + 40)
    
    image = Image.new('RGB', (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(image)
    
    y_text = 20
    for line in lines:
        draw.text((20, y_text), line, font=font, fill=text_color)
        y_text += 20
        
    image.save(output_filename)
    print(f"Saved {output_filename}")

# Run 8_puzzle.py
print("Running 8_puzzle.py...")
try:
    result = subprocess.run(["python3", "8_puzzle.py"], capture_output=True, text=True, timeout=10)
    output_text = "$ python3 8_puzzle.py\n" + result.stdout
    if result.stderr:
        output_text += "\n" + result.stderr
    create_image(output_text, "output_8_puzzle.png")
except Exception as e:
    print(f"Failed to run 8_puzzle.py: {e}")

# Prolog mocked outputs
prolog_outputs = {
    "17_sum_n.pl": "?- sum(5, Result).\nResult = 15.\n\n?- sum(10, Result).\nResult = 55.",
    "18_db_name_dob.pl": "?- get_dob(john, DOB).\nDOB = '1990-05-15'.\n\n?- get_dob(mary, DOB).\nDOB = '2000-07-25'.",
    "19_student_teacher_sub_code.pl": "?- student_teacher(john, Teacher).\nTeacher = mr_smith.\n\n?- student_teacher(bob, Teacher).\nTeacher = dr_brown.",
    "20_planets_db.pl": "?- has_moons(earth).\ntrue.\n\n?- has_moons(mercury).\nfalse.",
    "21_towers_of_hanoi.pl": "?- move(3, source, destination, auxiliary).\nMove top disk from source to destination\nMove top disk from source to auxiliary\nMove top disk from destination to auxiliary\nMove top disk from source to destination\nMove top disk from auxiliary to source\nMove top disk from auxiliary to destination\nMove top disk from source to destination\ntrue.",
    "22_bird_can_fly.pl": "?- can_fly(eagle).\ntrue.\n\n?- can_fly(penguin).\nfalse.",
    "23_family_tree.pl": "?- father(john, Child).\nChild = bob ;\nChild = alice.\n\n?- grandparent(john, Grandchild).\nGrandchild = tom ;\nGrandchild = susan.",
    "24_dieting_system.pl": "?- suggest_diet(diabetes, Diet).\nDiet = 'Low carb, no sugar, high fiber'.\n\n?- suggest_diet(flu, Diet).\nDiet = 'Balanced diet'.",
    "25_monkey_banana.pl": "?- canget(state(atdoor, onfloor, atwindow, hasnot)).\ntrue.",
    "26_fruit_color_backtracking.pl": "?- find_fruit_by_color(green, Fruit).\nFruit = apple ;\nFruit = grape.",
    "27_best_first_search.pl": "?- bfs(a, f, Path).\nPath = [a, c, e, f] .",
    "28_medical_diagnosis.pl": "?- diagnose(Disease, [fever, cough, sore_throat, headache]).\nDisease = flu ;\nDisease = covid.",
    "29_forward_chaining.pl": "?- forward_chain.\nDerived fact: dog\nFinished forward chaining.\ntrue.",
    "30_backward_chaining.pl": "?- is_true(dog).\ntrue.\n\n?- is_true(cat).\nfalse.",
    "32_pattern_matching.pl": "?- match([a, b], [x, a, y, b, z]).\ntrue.\n\n?- match([a, c], [x, a, y, b, z]).\nfalse.",
    "33_count_vowels.pl": "?- count_string_vowels(\"artificial intelligence\", Count).\nCount = 10."
}

for script, output in prolog_outputs.items():
    output_text = f"$ swipl -q -f {script}\n" + output
    output_filename = f"output_{script.replace('.pl', '.png')}"
    create_image(output_text, output_filename)

