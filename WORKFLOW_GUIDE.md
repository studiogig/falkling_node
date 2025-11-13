# 🎬 Kling Video Workflows Guide

## 📦 **2 Workflows Included**

### 1. **workflow_text_to_video.json**
Simple text-to-video generation using Kling Standard

### 2. **workflow_start_end_frame.json**
Advanced image-to-video with start and end frames using Kling Pro v1.6

---

## 🚀 **How to Load Workflows**

### In ComfyUI:
1. Click **"Load"** button (top menu)
2. Navigate to: `/Users/samhofman/Documents/ComfyUI-Kling-Video/`
3. Select either workflow JSON file
4. Click **Open**

OR

1. Drag and drop the JSON file directly into ComfyUI canvas

---

## 1️⃣ **TEXT-TO-VIDEO WORKFLOW**

### **What It Does**
Generates video from text description only - no images needed.

### **Workflow Components**
- **Kling Standard v1 Node**: The generator
- **ShowText Node**: Displays video URL

### **Step-by-Step Usage**

1. **Load the workflow**
   - File: `workflow_text_to_video.json`

2. **Edit the prompt** in Kling Standard node
   ```
   Examples:
   - "A golden retriever running through sunflowers at sunset"
   - "Drone shot flying over a misty mountain range, cinematic"
   - "Time-lapse of clouds moving over a city skyline"
   ```

3. **Set parameters**
   - **Duration**: 5 or 10 seconds
   - **Aspect Ratio**: 16:9, 9:16, or 1:1

4. **Queue Prompt** (button in top-right)

5. **Wait ~5 minutes** for generation
   - Watch console for progress

6. **Copy video URL** from ShowText node

7. **Download video**
   - Paste URL in browser
   - Right-click video → Save As

### **Pricing**
- ~$0.05-0.10 per 5 second video
- ~$0.10-0.20 per 10 second video

---

## 2️⃣ **START & END FRAME WORKFLOW**

### **What It Does**
Animates between two images - creates smooth transition from start to end frame.

### **Workflow Components**
- **2x LoadImage Nodes**: Start and end frames
- **Kling Pro v1.6 Node**: The generator (supports dual images)
- **ShowText Node**: Displays video URL

### **Step-by-Step Usage**

1. **Load the workflow**
   - File: `workflow_start_end_frame.json`

2. **Load START frame**
   - Click first LoadImage node
   - Upload your starting image
   - This will be frame 1 of the video

3. **Load END frame**
   - Click second LoadImage node
   - Upload your ending image
   - This will be the final frame

4. **Edit the prompt** in Kling Pro v1.6 node
   ```
   Focus on describing the TRANSITION/MOVEMENT:
   - "Camera slowly zooms out"
   - "Smooth transition with particles dissolving"
   - "Object rotates 360 degrees"
   - "Scene fades from day to night"
   ```

5. **Set parameters**
   - **Duration**: 5 or 10 seconds
   - **Aspect Ratio**: Must match your images!

6. **Queue Prompt**

7. **Wait ~5 minutes**

8. **Copy video URL** and download

### **Tips for Best Results**
✅ Use similar composition/style for both images
✅ Keep lighting consistent
✅ Same subject in both frames
✅ Describe the transition clearly in prompt

❌ Avoid drastically different images
❌ Don't use different aspect ratios

### **Pricing**
- ~$0.15-0.25 per 5 second video
- ~$0.30-0.50 per 10 second video

---

## 🎨 **PROMPT WRITING TIPS**

### **Good Prompts Include**
1. **Action/Movement**
   - "running", "flying", "zooming", "panning"

2. **Camera Work**
   - "slow zoom in", "camera orbits around"
   - "bird's eye view", "low angle shot"

3. **Style/Atmosphere**
   - "cinematic lighting", "golden hour"
   - "moody", "vibrant", "dreamlike"

4. **Details**
   - "wind blowing through hair"
   - "leaves falling", "water rippling"

### **Example Prompts**

**Landscape**
```
Aerial drone shot slowly rising over a misty valley at sunrise,
cinematic lighting, soft golden tones, peaceful atmosphere
```

**Product**
```
Camera slowly orbits around luxury watch on pedestal,
studio lighting, elegant reflections, premium look
```

**Character**
```
Portrait of woman with flowing hair, wind gently blowing,
soft backlight, cinematic color grading, shallow depth of field
```

---

## 🔧 **TROUBLESHOOTING**

### **"FAL_KEY not found"**
```bash
# Mac/Linux - Set your API key:
export FAL_KEY="your-api-key-here"

# Make it permanent:
echo 'export FAL_KEY="your-key"' >> ~/.zshrc
source ~/.zshrc
```

### **Video URL doesn't appear**
- Check console for errors
- Verify FAL_KEY is set correctly
- Check fal.ai account has credits
- Try simpler prompt

### **"Module not found: fal_client"**
```bash
# Install dependencies:
/Users/samhofman/Documents/ComfyUI/.venv/bin/python -m pip install -r /Users/samhofman/Documents/ComfyUI/custom_nodes/ComfyUI-Kling-Video/requirements.txt
```

### **Nodes don't appear in menu**
1. Verify installation path: `ComfyUI/custom_nodes/ComfyUI-Kling-Video`
2. Check all files are present
3. Restart ComfyUI completely
4. Check console for import errors

---

## 📊 **NODE COMPARISON**

| Node | Quality | Dual Images | Price | Best For |
|------|---------|-------------|-------|----------|
| **Kling Standard v1** | Good | ❌ | $ | Quick tests, drafts |
| **Kling Pro v1.0** | Great | ✅ | $$ | Quality animations |
| **Kling Pro v1.6** | Excellent | ✅ | $$ | Latest features |
| **Kling Master v2.0** | Premium | ❌ | $$$ | Final deliverables |

---

## 🎯 **WORKFLOW LOCATIONS**

All workflows saved in:
```
/Users/samhofman/Documents/ComfyUI-Kling-Video/
├── workflow_text_to_video.json
└── workflow_start_end_frame.json
```

---

## 🔗 **USEFUL LINKS**

- **Get API Key**: https://fal.ai/dashboard/keys
- **Kling Models**: https://fal.ai/models?search=kling
- **GitHub Repo**: https://github.com/studiogig/falkling_node

---

## 💡 **NEXT STEPS**

1. **Load a workflow** in ComfyUI
2. **Test with simple prompt** first
3. **Experiment with parameters**
4. **Save your favorite prompts**
5. **Share your results!**

Happy video generating! 🎬✨
