import os
import sys
from moviepy import (
    ColorClip,
    TextClip,
    CompositeVideoClip,
    concatenate_videoclips
)
# Import vfx to access the new effects framework in MoviePy 2.x
import moviepy.video.fx as vfx

class AnimationEngine:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.bg_color = (20, 20, 20)
        self.font_size = 40
        self.title_font_size = 60

        self.text_color = "white"
        self.title_color = "white"
        self.code_color = "#00FF00"      
        self.comment_color = "#808080"   

        self.fade_duration = 0.5
        
        self.font_family = self._get_safe_font(["Arial", "Helvetica", "DejaVuSans", "LiberationSans"])
        self.code_font_family = self._get_safe_font(["Courier New", "Courier", "DejaVuSansMono", "LiberationMono"])

    def _get_safe_font(self, font_options):
        if sys.platform.startswith("win"):
            if "Arial" in font_options and os.path.exists("C:/Windows/Fonts/arial.ttf"):
                return "C:/Windows/Fonts/arial.ttf"
            if "Courier New" in font_options and os.path.exists("C:/Windows/Fonts/cour.ttf"):
                return "C:/Windows/Fonts/cour.ttf"
        return font_options[0]

    def create_background(self, duration=3.0):
        return ColorClip(
            size=(self.width, self.height),
            color=self.bg_color,
            duration=duration
        )

    def create_title(self, text, duration=3.0):
        return TextClip(
            text=text,
            font_size=self.title_font_size,
            color=self.title_color,
            font=self.font_family,
            method="label",
            duration=duration
        )

    def create_text(self, text, color="white", fontsize=40, duration=3.0):
        return TextClip(
            text=text,
            font_size=fontsize,
            color=color,
            font=self.font_family,
            method="label",
            duration=duration
        )

    def create_code_text(self, text, duration=3.0):
        return TextClip(
            text=text,
            font_size=self.font_size,
            color=self.code_color,
            font=self.code_font_family,
            method="label",
            duration=duration
        )

    def create_fade_in(self, clip, duration=None):
        if not duration:
            duration = self.fade_duration
        
        # --- FIX: New MoviePy 2.x Effects API ---
        return clip.with_effects([vfx.FadeIn(duration)])


class PythonBasicsScene:
    def __init__(self, engine):
        self.engine = engine

    def create_intro_scene(self):
        intro_text = "Learn Python Programming"
        intro = self.engine.create_title(intro_text, duration=3.0)
        bg = self.engine.create_background(duration=3.0)
        
        positioned_intro = intro.with_position(("center", "center"))
        composite = CompositeVideoClip([bg, positioned_intro], size=(self.engine.width, self.engine.height))
        return self.engine.create_fade_in(composite)

    def variables_scene(self):
        bg = self.engine.create_background(duration=4.0)
        title = self.engine.create_title("Variables in Python", duration=4.0).with_position(("center", 40))
        explanation = self.engine.create_text("Variables store data in memory", duration=4.0).with_position(("center", "center"))
        code = self.engine.create_code_text("name = 'Python'", duration=4.0).with_position(("center", 500))

        return CompositeVideoClip([bg, title, explanation, code], size=(self.engine.width, self.engine.height))

    def functions_scene(self):
        bg = self.engine.create_background(duration=5.0)
        title = self.engine.create_title("Functions in Python", duration=5.0).with_position(("center", 40))
        explanation = self.engine.create_text("Functions are reusable blocks of code", duration=5.0).with_position(("center", 200))
        
        code_text = "def greet(name):\n    return 'Hello, ' + name\n\nprint(greet('Alice'))"
        code = self.engine.create_code_text(code_text, duration=5.0).with_position(("center", 400))

        return CompositeVideoClip([bg, title, explanation, code], size=(self.engine.width, self.engine.height))

    def lists_scene(self):
        bg = self.engine.create_background(duration=4.0)
        title = self.engine.create_title("Lists in Python", duration=4.0).with_position(("center", 40))
        
        code_text = "my_list = [1, 2, 3]\nprint(my_list[0])"
        code = self.engine.create_code_text(code_text, duration=4.0).with_position(("center", "center"))

        return CompositeVideoClip([bg, title, code], size=(self.engine.width, self.engine.height))

    def loops_scene(self):
        bg = self.engine.create_background(duration=4.0)
        title = self.engine.create_title("Loops in Python", duration=4.0).with_position(("center", 40))
        explanation = self.engine.create_text("Loops repeat code blocks", duration=4.0).with_position(("center", 200))
        
        code_text = "for i in range(3):\n    print('Iteration', i)"
        code = self.engine.create_code_text(code_text, duration=4.0).with_position(("center", 450))

        return CompositeVideoClip([bg, title, explanation, code], size=(self.engine.width, self.engine.height))


def main():
    engine = AnimationEngine()
    scene = PythonBasicsScene(engine)

    print("Assembling video clips...")
    final_video = concatenate_videoclips([
        scene.create_intro_scene(),
        scene.variables_scene(),
        scene.functions_scene(),
        scene.lists_scene(),
        scene.loops_scene()
    ], method="compose")

    print("Rendering final_video to disk...")
    final_video.write_videofile(
        "python_basics.mp4",
        fps=24,
        codec="libx264"
    )
    
    final_video.close()
    print("Done!")


if __name__ == "__main__":
    main()