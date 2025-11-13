# ComfyUI Kling Video Nodes

Clean, standalone implementation of Kling AI video generation nodes for ComfyUI, powered by [fal.ai](https://fal.ai).

## Features

✨ **4 Quality Tiers**
- **Standard v1** - Cost-effective baseline
- **Pro v1.0** - Enhanced quality with dual image support
- **Pro v1.6** - Latest Pro version
- **Master v2.0** - Premium quality

🎬 **Capabilities**
- Text-to-Video generation
- Image-to-Video animation
- Multiple aspect ratios (16:9, 9:16, 1:1)
- 5 or 10 second videos
- Tail image support (Pro versions)

## Installation

### Option 1: Git Clone (Recommended)

```bash
cd ~/path/to/ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-Kling-Video.git
cd ComfyUI-Kling-Video
pip install -r requirements.txt
```

### Option 2: Manual Install

1. Download this repository
2. Extract to `ComfyUI/custom_nodes/ComfyUI-Kling-Video`
3. Install dependencies:
```bash
pip install fal-client torch numpy pillow requests
```

## Configuration

### Set your fal.ai API Key

Get your API key from: https://fal.ai/dashboard/keys

**Mac/Linux:**
```bash
export FAL_KEY="your-api-key-here"
echo 'export FAL_KEY="your-key"' >> ~/.zshrc  # or ~/.bashrc
```

**Windows:**
```cmd
set FAL_KEY=your-api-key-here
```

## Usage

After installation and ComfyUI restart:

1. Right-click in ComfyUI canvas
2. Add Node → **Kling** → **Video**
3. Choose from 4 quality tiers:
   - Kling Standard v1
   - Kling Pro v1.0
   - Kling Pro v1.6
   - Kling Master v2.0

### Example Workflow

**Text-to-Video:**

1. Add "Kling Standard v1" node
2. Set prompt: "A golden retriever running through a field of sunflowers"
3. Duration: 5 seconds
4. Aspect ratio: 16:9
5. Queue Prompt
6. Video URL will be returned (download manually or use save node)

**Image-to-Video:**
1. Add "Kling Pro v1.6" node
2. Connect image input
3. Set prompt: "Camera slowly zooms in"
4. Duration: 5 seconds
5. Queue Prompt

## Node Parameters

### Common Parameters (All Nodes)
- **prompt** (required): Text description of desired video
- **duration** (required): 5 or 10 seconds
- **aspect_ratio** (required): 16:9, 9:16, or 1:1
- **image** (optional): Input image for image-to-video

### Pro-Only Parameters
- **tail_image** (optional): End frame for video (Pro v1.0 and v1.6 only)

## Pricing (Approximate)

Based on fal.ai pricing:
- **Standard v1**: ~$0.05-0.10 per 5s video
- **Pro v1.0/v1.6**: ~$0.15-0.25 per 5s video
- **Master v2.0**: ~$0.50-1.00 per 5s video

Check [fal.ai pricing](https://fal.ai/models/kling-video) for current rates.

## Troubleshooting

### "FAL_KEY not found"
Set the environment variable as shown in Configuration section.

### Nodes don't appear
1. Verify installation path: `ComfyUI/custom_nodes/ComfyUI-Kling-Video`
2. Check all files are present
3. Restart ComfyUI completely
4. Check console for import errors

### Video generation fails
1. Verify API key is correct
2. Check fal.ai account has credits
3. Try simpler prompt
4. Use Standard tier for testing

## Development

This is a standalone package with minimal dependencies:
- `fal_utils.py` - FAL API client and image utilities
- `kling_nodes.py` - 4 Kling node implementations
- `__init__.py` - ComfyUI node registration

## License

MIT License - See LICENSE file

## Credits

- Kling AI by Kuaishou Technology
- fal.ai API platform
- ComfyUI by comfyanonymous

## Links

- [fal.ai Dashboard](https://fal.ai/dashboard)
- [Kling Models](https://fal.ai/models?search=kling)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

---

**Author**: Sam Hofman  
**Repository**: https://github.com/yourusername/ComfyUI-Kling-Video
