# Assets

This directory contains static assets, media files, and resources for Browser Agent.

## Contents

### Images and Media
- **[img/](img/)** - Image assets and graphics
- **[desktop_screenshot.png](desktop_screenshot.png)** - Desktop application screenshot

### Directory Structure

```
assets/
├── img/                    # Image assets
│   ├── icons/             # Application icons
│   ├── logos/             # Brand logos and graphics
│   ├── screenshots/       # Application screenshots
│   └── ui/                # UI elements and graphics
├── fonts/                 # Custom fonts (if any)
├── audio/                 # Audio files (if any)
├── video/                 # Video files (if any)
└── documents/             # Static documents (PDFs, etc.)
```

## Asset Guidelines

### Image Assets

#### Formats
- **SVG** - Preferred for icons and simple graphics (scalable)
- **PNG** - For screenshots and complex images with transparency
- **JPG** - For photographs and complex images without transparency
- **WebP** - For web-optimized images (when supported)

#### Naming Conventions

```
# Icons
icon-{name}-{size}.{ext}
icon-browser-16.svg
icon-settings-24.png

# Screenshots
screenshot-{feature}-{date}.{ext}
screenshot-main-ui-2024-01-01.png
screenshot-browser-automation.png

# Logos
logo-{variant}-{size}.{ext}
logo-primary-256.svg
logo-monochrome-64.png

# UI Elements
ui-{component}-{state}.{ext}
ui-button-hover.svg
ui-progress-bar.png
```

#### Size Guidelines

| Type | Recommended Sizes | Format |
|------|------------------|--------|
| Icons | 16, 24, 32, 48, 64, 128, 256px | SVG, PNG |
| Logos | 64, 128, 256, 512px | SVG, PNG |
| Screenshots | Original resolution | PNG, JPG |
| UI Elements | As needed | SVG preferred |

### Optimization

#### Image Optimization

```bash
# Optimize PNG files
optipng -o7 assets/img/*.png

# Optimize JPG files
jpegoptim --max=85 assets/img/*.jpg

# Convert to WebP
cwebp -q 80 input.png -o output.webp

# Optimize SVG files
svgo assets/img/*.svg
```

#### File Size Guidelines

- **Icons**: < 10KB each
- **Screenshots**: < 500KB each
- **Logos**: < 50KB each
- **UI Elements**: < 25KB each

### Usage in Code

#### Python/GUI Applications

```python
from pathlib import Path

# Get asset path
ASSETS_DIR = Path(__file__).parent.parent / "assets"
ICON_PATH = ASSETS_DIR / "img" / "icons" / "app-icon.png"

# Load image in GUI framework
# Tkinter example
import tkinter as tk
from PIL import Image, ImageTk

image = Image.open(ICON_PATH)
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
```

#### Web Applications

```html
<!-- HTML -->  
<img src="/assets/img/logo-primary-256.svg" alt="Browser Agent Logo">

<!-- CSS -->
.icon {
    background-image: url('/assets/img/icons/browser-16.svg');
    background-size: 16px 16px;
}
```

#### Documentation

```markdown
<!-- Markdown -->
![Browser Agent Screenshot](assets/img/screenshots/main-ui.png)

<!-- Relative path from docs -->
![Logo](../assets/img/logo-primary-256.svg)
```

## Asset Management

### Adding New Assets

1. **Choose appropriate directory** based on asset type
2. **Follow naming conventions** for consistency
3. **Optimize file size** before adding
4. **Update documentation** if asset is referenced
5. **Consider licensing** and attribution requirements

### Asset Inventory

#### Current Assets

| File | Type | Size | Usage | Last Updated |
|------|------|------|-------|-------------|
| `desktop_screenshot.png` | Screenshot | ~XXX KB | Documentation | 2024-01-01 |
| `img/` | Directory | - | Various images | - |

#### Missing Assets (TODO)

- [ ] Application icon (multiple sizes)
- [ ] Logo variations (light/dark theme)
- [ ] UI mockups and wireframes
- [ ] Feature demonstration GIFs
- [ ] Social media preview images

### Version Control

#### What to Commit

✅ **DO commit:**
- Optimized images
- SVG files
- Small icons and logos
- Documentation images

❌ **DON'T commit:**
- Large video files (> 10MB)
- Unoptimized images
- Temporary/working files
- Generated thumbnails

#### Git LFS (Large File Storage)

For large assets, consider using Git LFS:

```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.png"
git lfs track "*.jpg"
git lfs track "*.mp4"

# Add .gitattributes
git add .gitattributes
```

### Licensing and Attribution

#### License Information

All assets should have clear licensing:

```
assets/
├── LICENSE.md              # Asset licensing information
├── ATTRIBUTION.md          # Third-party asset credits
└── img/
    ├── icons/
    │   ├── README.md       # Icon source and licensing
    │   └── browser-icon.svg
    └── screenshots/
        └── README.md       # Screenshot information
```

#### Attribution Template

```markdown
# Asset Attribution

## Icons
- **Browser Icon**: Created by [Author](link) - [License](license-link)
- **Settings Icon**: From [Icon Pack](link) - [License](license-link)

## Images
- **Background**: Photo by [Photographer](link) on [Source](link)

## Fonts
- **Custom Font**: [Font Name](link) - [License](license-link)
```

## Tools and Resources

### Image Editing

- **Vector Graphics**: Inkscape, Adobe Illustrator, Figma
- **Raster Graphics**: GIMP, Adobe Photoshop, Canva
- **Screenshots**: macOS Screenshot, Windows Snipping Tool, Flameshot
- **Optimization**: ImageOptim, TinyPNG, Squoosh

### Icon Resources

- **Free Icons**: Feather Icons, Heroicons, Lucide
- **Icon Fonts**: Font Awesome, Material Icons
- **Custom Icons**: Figma, Sketch, Adobe Illustrator

### Stock Images

- **Free**: Unsplash, Pexels, Pixabay
- **Paid**: Shutterstock, Getty Images, Adobe Stock

## Automation

### Asset Processing Scripts

```bash
#!/bin/bash
# scripts/optimize-assets.sh

echo "Optimizing assets..."

# Optimize PNG files
find assets/ -name "*.png" -exec optipng -o7 {} \;

# Optimize JPG files  
find assets/ -name "*.jpg" -exec jpegoptim --max=85 {} \;

# Optimize SVG files
find assets/ -name "*.svg" -exec svgo {} \;

echo "Asset optimization complete!"
```

### Build Integration

```python
# In build script
import subprocess
from pathlib import Path

def optimize_assets():
    """Optimize all assets during build process."""
    assets_dir = Path("assets")
    
    # Run optimization script
    subprocess.run(["bash", "scripts/optimize-assets.sh"])
    
    # Generate asset manifest
    generate_asset_manifest(assets_dir)

def generate_asset_manifest(assets_dir):
    """Generate manifest of all assets."""
    manifest = {}
    
    for asset in assets_dir.rglob("*"):
        if asset.is_file():
            manifest[str(asset)] = {
                "size": asset.stat().st_size,
                "modified": asset.stat().st_mtime
            }
    
    with open("assets/manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
```

## Best Practices

1. **Optimize for performance** - Compress images appropriately
2. **Use vector formats** when possible for scalability
3. **Maintain consistent style** across all visual assets
4. **Document asset sources** and licensing
5. **Version control appropriately** - use Git LFS for large files
6. **Organize logically** - group related assets together
7. **Name descriptively** - use clear, consistent naming
8. **Consider accessibility** - provide alt text and descriptions

## Troubleshooting

### Common Issues

1. **Large file sizes**
   ```bash
   # Check file sizes
   find assets/ -type f -exec ls -lh {} \; | sort -k5 -hr
   
   # Optimize large files
   optipng -o7 large-image.png
   ```

2. **Missing assets in build**
   ```bash
   # Verify assets exist
   ls -la assets/img/
   
   # Check build configuration
   grep -r "assets/" build-config
   ```

3. **Broken image links**
   ```bash
   # Find broken references
   grep -r "assets/" . --include="*.py" --include="*.html" --include="*.md"
   ```

### Getting Help

- Check file paths and naming conventions
- Verify image formats and optimization
- Review licensing and attribution requirements
- See [../docs/CONTRIBUTING.md](../docs/CONTRIBUTING.md) for development guidelines
- Open an issue for asset-related problems

---

**Note:** Always optimize assets for performance while maintaining visual quality appropriate for their intended use.