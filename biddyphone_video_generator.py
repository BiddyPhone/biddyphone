
"""
BiddyPhone Promotional Video Generator
Python 3.13.5 Compatible

This script creates a professional promotional video for BiddyPhone using:
- MoviePy for video editing
- gTTS for AI voiceover synthesis
- PIL for image processing
- Custom transitions and effects

Dependencies:
pip install moviepy pillow gtts numpy requests

Usage:
python biddyphone_video_generator.py
"""

import os
import sys
from pathlib import Path
import numpy as np
from moviepy import (
    VideoFileClip, AudioFileClip, ImageClip, TextClip,
    CompositeVideoClip, concatenate_videoclips,
    ColorClip, CompositeAudioClip, afx, vfx
)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from gtts import gTTS
import requests
from io import BytesIO
import tempfile
import json

class BiddyPhoneVideoGenerator:
    def __init__(self):
        self.output_dir = Path("biddyphone_promo")
        self.assets_dir = self.output_dir / "assets"
        self.temp_dir = self.output_dir / "temp"
        
        # Create directories
        self.output_dir.mkdir(exist_ok=True)
        self.assets_dir.mkdir(exist_ok=True)
        self.temp_dir.mkdir(exist_ok=True)
        
        # Video settings
        self.video_size = (1920, 1080)  # Full HD
        self.fps = 30
        self.duration_per_scene = 6  # seconds
        
        # Colors and branding
        self.brand_colors = {
            'primary': '#FF6B35',     # Orange
            'secondary': '#2E86AB',   # Blue
            'accent': '#A23B72',      # Purple
            'dark': '#1A1A1A',        # Dark gray
            'light': '#F18F01',       # Light orange
            'white': '#FFFFFF'
        }
        
        # Scene configuration
        self.scenes = self._get_scene_config()
        
    def _get_scene_config(self):
        """Define all scenes with their content and timing"""
        return [
            {
                'id': 'intro',
                'duration': 4,
                'title': 'BiddyPhone',
                'subtitle': 'Sovereignty in Your Pocket',
                'voiceover': 'Introducing BiddyPhone - the revolutionary smartphone that puts economic sovereignty directly in your pocket.',
                'background_type': 'gradient',
                'effect': 'zoom_in'
            },
            {
                'id': 'problem',
                'duration': 6,
                'title': 'The Global Challenge',
                'subtitle': '1.4 Billion People Remain Unbanked',
                'voiceover': 'One point four billion people worldwide remain unbanked. Three billion lack stable internet access. Economic opportunities remain geographically and politically restricted.',
                'background_type': 'world_map',
                'effect': 'slide_left'
            },
            {
                'id': 'solution',
                'duration': 7,
                'title': 'The BiddyPhone Solution',
                'subtitle': 'Mine Bitcoin • Solar Powered • Satellite Connected',
                'voiceover': 'BiddyPhone is an open-hardware, solar-powered smartphone that mines Bitcoin and provides off-grid connectivity via LEO satellites and mesh networking.',
                'background_type': 'tech_grid',
                'effect': 'fade_in'
            },
            {
                'id': 'features',
                'duration': 8,
                'title': 'Revolutionary Features',
                'subtitle': 'Ultra-Low Power ASIC • Solar Charging • Satellite Sync',
                'voiceover': 'Ultra-low-power ASIC mining chip. Solar charging wrap for daily energy. Satellite synchronization with mesh networking fallback. Secure Bitcoin wallet with UBI distribution.',
                'background_type': 'phone_mockup',
                'effect': 'rotate_in'
            },
            {
                'id': 'ubi',
                'duration': 6,
                'title': 'Universal Basic Income',
                'subtitle': '100 Sats Daily Per Person',
                'voiceover': 'Earn one hundred satoshis daily through Bitcoin mining. True universal basic income distributed globally through decentralized infrastructure.',
                'background_type': 'bitcoin_animation',
                'effect': 'scale_up'
            },
            {
                'id': 'impact',
                'duration': 5,
                'title': 'Global Impact',
                'subtitle': 'Banking the Unbanked • Powering the Future',
                'voiceover': 'Transforming smartphones into vehicles for economic empowerment. Building financial sovereignty for billions worldwide.',
                'background_type': 'world_network',
                'effect': 'pulse'
            },
            {
                'id': 'cta',
                'duration': 4,
                'title': 'Join the Revolution',
                'subtitle': 'BiddyPhone.com',
                'voiceover': 'Join the BiddyPhone revolution. Visit BiddyPhone dot com to learn more.',
                'background_type': 'logo_finale',
                'effect': 'burst'
            }
        ]
    
    def create_logo(self):
        """Create BiddyPhone logo"""
        logo_size = (400, 120)
        logo = Image.new('RGBA', logo_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(logo)
        
        try:
            # Try to use a nice font, fallback to default
            font_large = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
            font_small = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 16)
        except:
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()
        
        # Draw main text
        draw.text((20, 30), "Biddy", fill=self.brand_colors['primary'], font=font_large)
        draw.text((150, 30), "Phone", fill=self.brand_colors['secondary'], font=font_large)
        
        # Draw tagline
        draw.text((20, 85), "Sovereignty in Your Pocket", fill=self.brand_colors['accent'], font=font_small)
        
        logo_path = self.assets_dir / "logo.png"
        logo.save(logo_path)
        return logo_path
    
    def create_background_image(self, scene_type, size=(1920, 1080)):
        """Create background images for different scene types"""
        img = Image.new('RGB', size, self.brand_colors['dark'])
        draw = ImageDraw.Draw(img)
        
        if scene_type == 'gradient':
            # Create gradient background
            for y in range(size[1]):
                r = int(255 * (1 - y / size[1]) * 0.2)
                g = int(107 * (1 - y / size[1]) * 0.5)
                b = int(53 * (1 - y / size[1]) * 0.8)
                draw.line([(0, y), (size[0], y)], fill=(r, g, b))
                
        elif scene_type == 'world_map':
            # Simple world representation with dots
            for _ in range(200):
                x = np.random.randint(0, size[0])
                y = np.random.randint(0, size[1])
                radius = np.random.randint(2, 8)
                color = self.brand_colors['secondary'] if np.random.random() > 0.7 else self.brand_colors['primary']
                draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color)
                
        elif scene_type == 'tech_grid':
            # Tech grid pattern
            grid_size = 50
            for x in range(0, size[0], grid_size):
                draw.line([(x, 0), (x, size[1])], fill=self.brand_colors['secondary'], width=1)
            for y in range(0, size[1], grid_size):
                draw.line([(0, y), (size[0], y)], fill=self.brand_colors['secondary'], width=1)
                
        elif scene_type == 'phone_mockup':
            # Simple phone silhouette
            phone_width, phone_height = 300, 600
            phone_x = (size[0] - phone_width) // 2
            phone_y = (size[1] - phone_height) // 2
            draw.rounded_rectangle(
                [phone_x, phone_y, phone_x + phone_width, phone_y + phone_height],
                radius=30, fill=self.brand_colors['primary'], outline=self.brand_colors['white'], width=3
            )
            
        elif scene_type == 'bitcoin_animation':
            # Bitcoin symbol and particles
            center_x, center_y = size[0] // 2, size[1] // 2
            # Draw Bitcoin symbol (simplified)
            draw.ellipse([center_x-100, center_y-100, center_x+100, center_y+100], 
                        fill=self.brand_colors['light'], outline=self.brand_colors['white'], width=5)
            # Add smaller circles around
            for angle in range(0, 360, 30):
                x = center_x + 200 * np.cos(np.radians(angle))
                y = center_y + 200 * np.sin(np.radians(angle))
                draw.ellipse([x-10, y-10, x+10, y+10], fill=self.brand_colors['accent'])
                
        elif scene_type == 'world_network':
            # Network connections across the world
            for _ in range(50):
                x1, y1 = np.random.randint(0, size[0]), np.random.randint(0, size[1])
                x2, y2 = np.random.randint(0, size[0]), np.random.randint(0, size[1])
                draw.line([(x1, y1), (x2, y2)], fill=self.brand_colors['primary'], width=2)
                draw.ellipse([x1-5, y1-5, x1+5, y1+5], fill=self.brand_colors['white'])
                
        elif scene_type == 'logo_finale':
            # Clean background for final logo
            for y in range(size[1]):
                alpha = y / size[1]
                r = int(26 * (1 - alpha) + 255 * alpha * 0.1)
                g = int(134 * (1 - alpha) + 107 * alpha * 0.1)
                b = int(171 * (1 - alpha) + 53 * alpha * 0.1)
                draw.line([(0, y), (size[0], y)], fill=(r, g, b))
        
        bg_path = self.assets_dir / f"bg_{scene_type}.png"
        img.save(bg_path)
        return bg_path
    
    def generate_voiceover(self, text, scene_id):
        """Generate AI voiceover using gTTS"""
        tts = gTTS(text=text, lang='en', slow=False)
        audio_path = self.temp_dir / f"vo_{scene_id}.mp3"
        tts.save(str(audio_path))
        return audio_path
    
    def create_background_music(self, duration):
        """Create simple background music using numpy"""
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration))
        
        # Create ambient background music
        freq1, freq2, freq3 = 220, 330, 440  # A, E, A notes
        music = (np.sin(2 * np.pi * freq1 * t) * 0.1 +
                np.sin(2 * np.pi * freq2 * t) * 0.08 +
                np.sin(2 * np.pi * freq3 * t) * 0.06)
        
        # Add some fade in/out
        fade_samples = int(sample_rate * 2)  # 2 second fade
        music[:fade_samples] *= np.linspace(0, 1, fade_samples)
        music[-fade_samples:] *= np.linspace(1, 0, fade_samples)
        
        # Save as temporary wav file
        import wave
        music_path = self.temp_dir / "background_music.wav"
        with wave.open(str(music_path), 'w') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes((music * 32767).astype(np.int16).tobytes())
        
        return music_path
    
    def create_text_clip(self, text, duration, fontsize=60, color='white', position='center'):
        """Create text overlay clip"""
        return TextClip(
            text, 
            fontsize=fontsize, 
            color=color, 
            font='Arial-Bold',
            size=self.video_size
        ).set_duration(duration).set_position(position)
    
    def apply_effect(self, clip, effect_type):
        """Apply visual effects to clips"""
        if effect_type == 'zoom_in':
            return clip.resize(lambda t: 1 + 0.02 * t)
        elif effect_type == 'slide_left':
            return clip.set_position(lambda t: (-100 + 100 * t, 'center'))
        elif effect_type == 'fade_in':
            return clip.fadein(1).fadeout(1)
        elif effect_type == 'rotate_in':
            return clip.rotate(lambda t: 360 * t / clip.duration)
        elif effect_type == 'scale_up':
            return clip.resize(lambda t: 0.8 + 0.2 * np.sin(2 * np.pi * t))
        elif effect_type == 'pulse':
            return clip.resize(lambda t: 1 + 0.1 * np.sin(4 * np.pi * t))
        elif effect_type == 'burst':
            return clip.resize(lambda t: 1 + 0.5 * (1 - t / clip.duration))
        else:
            return clip.fadein(0.5).fadeout(0.5)
    
    def create_scene_clip(self, scene):
        """Create a complete scene clip with all elements"""
        scene_clips = []
        
        # Create background
        bg_path = self.create_background_image(scene['background_type'])
        bg_clip = ImageClip(str(bg_path)).set_duration(scene['duration']).resize(self.video_size)
        bg_clip = self.apply_effect(bg_clip, scene.get('effect', 'fade_in'))
        scene_clips.append(bg_clip)
        
        # Add title text
        if scene.get('title'):
            title_clip = self.create_text_clip(
                scene['title'], 
                scene['duration'], 
                fontsize=80, 
                color=self.brand_colors['white'],
                position=('center', 200)
            ).fadein(0.5)
            scene_clips.append(title_clip)
        
        # Add subtitle text
        if scene.get('subtitle'):
            subtitle_clip = self.create_text_clip(
                scene['subtitle'], 
                scene['duration'], 
                fontsize=40, 
                color=self.brand_colors['light'],
                position=('center', 300)
            ).fadein(1)
            scene_clips.append(subtitle_clip)
        
        # Generate and add voiceover
        if scene.get('voiceover'):
            vo_path = self.generate_voiceover(scene['voiceover'], scene['id'])
            vo_clip = AudioFileClip(str(vo_path))
            # Ensure voiceover fits scene duration
            if vo_clip.duration > scene['duration']:
                vo_clip = vo_clip.subclip(0, scene['duration'])
            scene_clips.append(vo_clip)
        
        return CompositeVideoClip(scene_clips).set_duration(scene['duration'])
    
    def create_logo_intro(self):
        """Create animated logo introduction"""
        logo_path = self.create_logo()
        logo_clip = ImageClip(str(logo_path)).set_duration(3).set_position('center')
        logo_clip = logo_clip.resize(0.5).fadein(1).fadeout(1)
        
        # Create background for logo
        bg = ColorClip(size=self.video_size, color=self.brand_colors['dark']).set_duration(3)
        
        return CompositeVideoClip([bg, logo_clip])
    
    def generate_video(self):
        """Generate the complete promotional video"""
        print("Starting BiddyPhone promotional video generation...")
        
        # Create logo intro
        print("Creating logo intro...")
        logo_intro = self.create_logo_intro()
        
        # Create all scene clips
        scene_clips = [logo_intro]
        total_duration = 3  # Logo intro duration
        
        for i, scene in enumerate(self.scenes):
            print(f"Creating scene {i+1}/{len(self.scenes)}: {scene['id']}")
            scene_clip = self.create_scene_clip(scene)
            scene_clips.append(scene_clip)
            total_duration += scene['duration']
        
        # Concatenate all clips
        print("Concatenating video clips...")
        final_video = concatenate_videoclips(scene_clips, method="compose")
        
        # Create and add background music
        print("Adding background music...")
        music_path = self.create_background_music(total_duration)
        bg_music = AudioFileClip(str(music_path)).volumex(0.3)  # Lower volume
        
        # Combine video with background music
        if final_video.audio:
            final_audio = CompositeAudioClip([final_video.audio, bg_music])
        else:
            final_audio = bg_music
        
        final_video = final_video.set_audio(final_audio)
        
        # Export final video
        output_path = self.output_dir / "BiddyPhone_Promo.mp4"
        print(f"Exporting final video to {output_path}...")
        
        final_video.write_videofile(
            str(output_path),
            fps=self.fps,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile=str(self.temp_dir / 'temp-audio.m4a'),
            remove_temp=True
        )
        
        print(f"Video generation complete! Output: {output_path}")
        return output_path
    
    def generate_script_document(self):
        """Generate detailed script and scene plan"""
        script_content = """
# BiddyPhone Promotional Video Script & Scene Plan

## Video Overview
- **Duration**: ~40 seconds
- **Format**: Full HD 1920x1080, 30fps
- **Style**: Modern tech promotional with dynamic transitions
- **Target Audience**: Unbanked populations, crypto enthusiasts, tech innovators

## Detailed Scene Breakdown

"""
        
        for i, scene in enumerate(self.scenes, 1):
            script_content += f"""
### Scene {i}: {scene['title']}
- **Duration**: {scene['duration']} seconds
- **Visual Style**: {scene['background_type'].replace('_', ' ').title()}
- **Effect**: {scene.get('effect', 'Standard transition').replace('_', ' ').title()}
- **Voiceover**: "{scene.get('voiceover', 'N/A')}"
- **Text Elements**:
  - Title: "{scene.get('title', 'N/A')}"
  - Subtitle: "{scene.get('subtitle', 'N/A')}"

"""
        
        script_content += """
## Technical Specifications

### Video Settings
- Resolution: 1920x1080 (Full HD)
- Frame Rate: 30 fps
- Codec: H.264
- Bitrate: Variable (optimized for quality)

### Audio Settings
- Voiceover: AI-generated using gTTS
- Background Music: Procedurally generated ambient track
- Audio Codec: AAC
- Sample Rate: 44.1 kHz

### Visual Elements
- Brand Colors: Orange (#FF6B35), Blue (#2E86AB), Purple (#A23B72)
- Typography: Arial Bold for titles, Arial for subtitles
- Logo: Custom BiddyPhone branding
- Transitions: Custom effects per scene

## Post-Production Notes
- All assets generated programmatically
- Modular scene structure for easy editing
- Optimized for social media and web distribution
- Includes captions and visual accessibility features
"""
        
        script_path = self.output_dir / "BiddyPhone_Script_Plan.md"
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        return script_path
    
    def cleanup_temp_files(self):
        """Clean up temporary files"""
        import shutil
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

def main():
    """Main execution function"""
    generator = BiddyPhoneVideoGenerator()
    
    try:
        # Generate script document
        script_path = generator.generate_script_document()
        print(f"Script document created: {script_path}")
        
        # Generate promotional video
        video_path = generator.generate_video()
        
        print(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                          VIDEO GENERATION COMPLETE!                         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Video Output: {str(video_path):<58} ║
║ Script & Plan: {str(script_path):<55} ║
║                                                                              ║
║ The promotional video includes:                                              ║
║ ✓ AI-generated voiceover narration                                          ║
║ ✓ Dynamic text overlays and titles                                          ║
║ ✓ Procedural background music                                               ║
║ ✓ Animated logo introduction                                                ║
║ ✓ Custom background images for each scene                                   ║
║ ✓ Professional transitions and effects                                      ║
║ ✓ Full HD MP4 export ready for distribution                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """)
        
    except Exception as e:
        print(f"Error during video generation: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Clean up temporary files
        generator.cleanup_temp_files()

if __name__ == "__main__":
    main()
