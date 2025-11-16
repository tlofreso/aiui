# DaisyUI Feedback UI Skill

A Claude skill for generating lightweight, focused UI components using DaisyUI for collecting human feedback during agentic workflows.

## What This Skill Does

This skill helps Claude generate minimal, single-purpose UI components (modals, forms, inputs) for pausing agentic workflows to collect user input. These are not full webpages but lightweight elements similar to Slack channel interactions.

**Use this skill when you need to:**
- Ask the user a question during workflow execution
- Collect a single piece of input or decision
- Confirm before taking an action
- Show progress or status
- Display success/error feedback

## File Structure

```
daisyui-feedback-ui/
├── SKILL.md       # Main skill (start here)
├── ADVANCED.md    # Advanced patterns (multi-step, loading, etc.)
├── TEMPLATES.md   # Ready-to-use complete HTML templates
└── README.md      # This file
```

## Quick Start

1. **For simple components**: Read SKILL.md and use the component patterns
2. **For complex scenarios**: Check ADVANCED.md for multi-step, loading states, etc.
3. **For quick copy-paste**: Use TEMPLATES.md for complete HTML files

## Design Philosophy

**One question per component** - Each UI should collect exactly one piece of information

**Show context inline** - Display relevant conversation context within the component

**Always provide escape** - Include Cancel, Skip, or Back options

**Constrain inputs** - Use dropdowns/radio instead of free text when possible

**Smart defaults** - Pre-select reasonable options based on context

## Example Usage

### Scenario: Deploying to Production

Agent needs confirmation before deploying:

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Deploy to Production?</h3>
    <p class="py-4">
      Ready to deploy <strong>v2.1.3</strong>. All tests passed.
    </p>
    <div class="modal-action">
      <button class="btn btn-primary">Deploy</button>
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

## Component Types Available

**Input Collection:**
- Dropdown selection (priority, status, categories)
- Text input (names, titles, short descriptions)
- Textarea (longer responses, comments)
- Radio buttons (2-4 mutually exclusive options)
- Checkboxes (multiple selections)
- Numeric input (counts, timeouts, thresholds)
- Date/time pickers (scheduling)
- File upload (attachments, configs)

**Feedback & Status:**
- Confirmation dialogs (with warnings for destructive actions)
- Success/error messages
- Loading indicators (spinners, progress bars)
- Toast notifications (non-blocking feedback)

**Context Display:**
- Cards (showing context)
- Badges (status, counts, tags)
- Alerts (info, warning, error)
- Timeline (event history)
- Collapsible details (progressive disclosure)

## Installation

### For Claude Code

1. Copy the `daisyui-feedback-ui` directory to your skills folder:
   - Personal: `~/.claude/skills/`
   - Project: `.claude/skills/`

2. The skill will be automatically discovered by Claude Code

### For Claude Agent SDK

1. Add the skill directory to your project
2. Reference it in your agent configuration

### For Claude API

1. Upload the skill using the Skills API
2. Reference it in your API requests

## DaisyUI Setup

All components require the DaisyUI CDN in your HTML:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <!-- Your component here -->
</body>
</html>
```

No npm install required - uses CDN only.

## Customization

**Themes:**
Change `data-theme` attribute on `<html>` tag:
- `light`, `dark` (most common)
- `cupcake`, `corporate`, `business`, `cyberpunk`, etc.

**Colors:**
- `btn-primary` (blue) - Main action
- `btn-secondary` (purple) - Alternative
- `btn-error` (red) - Destructive
- `btn-success` (green) - Positive

**Sizes:**
- `btn-sm`, `input-sm` - Small
- `btn-md`, `input-md` - Default
- `btn-lg`, `input-lg` - Large

## Common Patterns

### Asking for Confirmation

```html
<div class="modal-box">
  <h3 class="font-bold text-lg">Confirm Action?</h3>
  <p class="py-4">Context about what will happen</p>
  <div class="modal-action">
    <button class="btn btn-primary">Confirm</button>
    <button class="btn">Cancel</button>
  </div>
</div>
```

### Collecting Text Input

```html
<div class="modal-box">
  <h3 class="font-bold text-lg">Enter Name</h3>
  <input type="text" placeholder="..." class="input input-bordered w-full" />
  <div class="modal-action">
    <button class="btn btn-primary">Submit</button>
    <button class="btn">Skip</button>
  </div>
</div>
```

### Showing Success

```html
<div class="alert alert-success">
  <span>✓ Operation completed successfully!</span>
</div>
```

## Anti-Patterns to Avoid

❌ Multiple unrelated questions in one modal
❌ Missing context (user must remember)
❌ No cancel/escape option
❌ Free text when constrained choices would work
❌ Unclear which button is primary action
❌ Technical jargon instead of natural language

## Testing Components

Before using a component, verify:
1. **One question** - Collects exactly one piece of information
2. **Context visible** - User can see what this relates to
3. **Primary action clear** - Obvious which button to press
4. **Escape route** - Has Cancel/Skip/Back option
5. **Mobile-friendly** - Text isn't too long (DaisyUI handles responsive)
6. **Smart default** - Pre-selected sensible option

## Resources

- [DaisyUI Documentation](https://daisyui.com/)
- [DaisyUI Components](https://daisyui.com/components/)
- [DaisyUI Themes](https://daisyui.com/docs/themes/)
- [Tailwind CSS](https://tailwindcss.com/)

## Version

Skill version: 1.0
DaisyUI version: 4.12.14 (via CDN)

## License

This skill is provided as-is for use with Claude products.
