---
name: daisyui-feedback-ui
description: Generate lightweight, focused UI components using DaisyUI for collecting human feedback during agentic workflows. Use when you need to pause execution to ask the user a question, collect input, or confirm a decision. Ideal for modals, forms, single-input dialogs, and confirmation prompts.
---

# DaisyUI Feedback UI

Generate minimal, focused UI components for human-in-the-loop interactions during agentic workflows. These are not full applications but lightweight elements for collecting single decisions or inputs.

## Quick Start

Always include DaisyUI CDN in your HTML:

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

## Core Design Rules

**One question per component** - Each UI should collect exactly one piece of information or decision

**Show context inline** - Display relevant information from the conversation within the component

**Always provide escape** - Include Cancel, Skip, or Back options

**Constrain inputs** - Use dropdowns/radio buttons instead of free text when possible

**Smart defaults** - Pre-select reasonable options based on context

## Component Patterns

### Selection (Choose One Option)

Use for: Priority levels, status values, predefined categories

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Select Priority</h3>
    <p class="py-4">For task: <strong>Fix login authentication bug</strong></p>
    
    <select class="select select-bordered w-full max-w-xs">
      <option>Low</option>
      <option selected>Medium</option>
      <option>High</option>
      <option>Critical</option>
    </select>
    
    <div class="modal-action">
      <button class="btn btn-primary">Confirm</button>
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

**Alternative: Radio buttons for 2-4 options**

```html
<div class="form-control">
  <label class="label cursor-pointer">
    <span class="label-text">High Priority</span>
    <input type="radio" name="priority" class="radio radio-primary" />
  </label>
  <label class="label cursor-pointer">
    <span class="label-text">Normal Priority</span>
    <input type="radio" name="priority" class="radio radio-primary" checked />
  </label>
  <label class="label cursor-pointer">
    <span class="label-text">Low Priority</span>
    <input type="radio" name="priority" class="radio radio-primary" />
  </label>
</div>
```

### Text Input (Short Response)

Use for: Names, titles, short descriptions, IDs

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Name This Feature</h3>
    <p class="py-4">Creating authentication module for the user dashboard</p>
    
    <input 
      type="text" 
      placeholder="e.g., OAuth Integration" 
      class="input input-bordered w-full" 
      value="User Authentication"
    />
    <label class="label">
      <span class="label-text-alt">Used for file naming and documentation</span>
    </label>
    
    <div class="modal-action">
      <button class="btn btn-primary">Continue</button>
      <button class="btn">Skip</button>
    </div>
  </div>
</div>
```

### Textarea (Longer Response)

Use for: Descriptions, feedback, comments, explanations

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Add Context</h3>
    <p class="py-4">Why should we prioritize this bug fix?</p>
    
    <textarea 
      class="textarea textarea-bordered w-full h-24" 
      placeholder="Explain the impact or urgency..."
    ></textarea>
    
    <div class="modal-action">
      <button class="btn btn-primary">Submit</button>
      <button class="btn">Skip</button>
    </div>
  </div>
</div>
```

### Confirmation Dialog

Use for: Destructive actions, significant decisions, point of no return

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">⚠️ Confirm Action</h3>
    <p class="py-4">
      This will delete <strong>127 test files</strong> from the repository. 
      This action cannot be undone.
    </p>
    
    <div class="alert alert-warning">
      <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
      </svg>
      <span>Files will be permanently deleted</span>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-error">Delete Files</button>
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

### Multiple Selection

Use for: Tags, features, options where multiple choices are valid

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Select Test Types</h3>
    <p class="py-4">Which tests should run before deployment?</p>
    
    <div class="form-control">
      <label class="label cursor-pointer">
        <span class="label-text">Unit Tests</span>
        <input type="checkbox" checked class="checkbox checkbox-primary" />
      </label>
      <label class="label cursor-pointer">
        <span class="label-text">Integration Tests</span>
        <input type="checkbox" checked class="checkbox checkbox-primary" />
      </label>
      <label class="label cursor-pointer">
        <span class="label-text">E2E Tests</span>
        <input type="checkbox" class="checkbox checkbox-primary" />
      </label>
      <label class="label cursor-pointer">
        <span class="label-text">Performance Tests</span>
        <input type="checkbox" class="checkbox checkbox-primary" />
      </label>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">Run Selected Tests</button>
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

### Numeric Input

Use for: Counts, durations, percentages, quantities

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Set Timeout</h3>
    <p class="py-4">How long should we wait for the API response?</p>
    
    <div class="form-control">
      <label class="label">
        <span class="label-text">Seconds</span>
      </label>
      <input 
        type="number" 
        value="30" 
        min="1" 
        max="300"
        class="input input-bordered w-full max-w-xs" 
      />
      <label class="label">
        <span class="label-text-alt">Range: 1-300 seconds</span>
      </label>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">Set Timeout</button>
      <button class="btn">Use Default (30s)</button>
    </div>
  </div>
</div>
```

**Alternative: Range slider for approximate values**

```html
<div class="form-control">
  <label class="label">
    <span class="label-text">Confidence Threshold: <strong>75%</strong></span>
  </label>
  <input 
    type="range" 
    min="0" 
    max="100" 
    value="75" 
    class="range range-primary" 
  />
  <div class="w-full flex justify-between text-xs px-2">
    <span>0%</span>
    <span>50%</span>
    <span>100%</span>
  </div>
</div>
```

### Progress Indicator

Use for: Multi-step processes, showing what's next

```html
<div class="card w-96 bg-base-100 shadow-xl">
  <div class="card-body">
    <h2 class="card-title">Deployment Progress</h2>
    
    <ul class="steps steps-vertical">
      <li class="step step-primary">Build Complete</li>
      <li class="step step-primary">Tests Passed</li>
      <li class="step">Awaiting Approval</li>
      <li class="step">Deploy to Production</li>
    </ul>
    
    <div class="card-actions justify-end mt-4">
      <button class="btn btn-primary">Approve & Deploy</button>
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

### Success Feedback

Use for: Confirming action completion, showing results

```html
<div class="modal modal-open">
  <div class="modal-box">
    <div class="alert alert-success">
      <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      <span>Successfully deployed to production!</span>
    </div>
    
    <div class="py-4">
      <p><strong>URL:</strong> https://app.example.com</p>
      <p><strong>Version:</strong> v2.1.3</p>
      <p><strong>Time:</strong> 2m 34s</p>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">View Deployment</button>
      <button class="btn">Close</button>
    </div>
  </div>
</div>
```

## DaisyUI Class Reference

**Modals:**
- `modal` - Base modal component
- `modal-open` - Makes modal visible
- `modal-box` - Content container
- `modal-action` - Button row at bottom

**Buttons:**
- `btn` - Base button
- `btn-primary` - Main action (blue)
- `btn-secondary` - Alternative action (purple)
- `btn-error` - Destructive action (red)
- `btn-ghost` - Subtle action

**Form Elements:**
- `input input-bordered` - Text input with border
- `select select-bordered` - Dropdown
- `textarea textarea-bordered` - Multi-line text
- `checkbox checkbox-primary` - Checkbox
- `radio radio-primary` - Radio button
- `range range-primary` - Slider
- `form-control` - Wrapper for form fields
- `label` - Form label wrapper
- `label-text` - Label text
- `label-text-alt` - Helper text

**Alerts:**
- `alert` - Base alert
- `alert-info` - Information (blue)
- `alert-success` - Success (green)
- `alert-warning` - Warning (yellow)
- `alert-error` - Error (red)

**Cards:**
- `card` - Container
- `card-body` - Content area
- `card-title` - Title text
- `card-actions` - Button area

**Progress:**
- `steps` - Step indicator
- `steps-vertical` - Vertical orientation
- `step` - Individual step
- `step-primary` - Completed step

## Anti-Patterns

❌ **Multiple unrelated questions in one modal**
```html
<!-- DON'T: Too many unrelated inputs -->
<div class="modal-box">
  <input placeholder="Project name" />
  <select><!-- Priority --></select>
  <textarea placeholder="Description"></textarea>
  <input type="date" />
</div>
```

✅ **One focused question per component**
```html
<!-- DO: Single decision point -->
<div class="modal-box">
  <h3>Select Priority</h3>
  <select><!-- Just priority --></select>
</div>
```

❌ **Missing context - user must remember**
```html
<!-- DON'T: No context -->
<h3>Choose an option</h3>
<select>
  <option>Option A</option>
  <option>Option B</option>
</select>
```

✅ **Context shown inline**
```html
<!-- DO: Show what this is for -->
<h3>Deployment Strategy</h3>
<p>For release v2.1.3 to production</p>
<select>
  <option>Blue-Green</option>
  <option>Rolling</option>
</select>
```

❌ **No escape option**
```html
<!-- DON'T: Only one button -->
<div class="modal-action">
  <button class="btn btn-primary">Confirm</button>
</div>
```

✅ **Always provide cancel/skip**
```html
<!-- DO: Give user a way out -->
<div class="modal-action">
  <button class="btn btn-primary">Confirm</button>
  <button class="btn">Cancel</button>
</div>
```

❌ **Free text when constrained options exist**
```html
<!-- DON'T: Open text for limited options -->
<input type="text" placeholder="Enter priority (high/medium/low)" />
```

✅ **Use dropdowns/radio for known options**
```html
<!-- DO: Constrain choices -->
<select class="select select-bordered">
  <option>High</option>
  <option>Medium</option>
  <option>Low</option>
</select>
```

## Testing Your Component

Before using a component, verify:

1. **One question** - Does this collect exactly one piece of information?
2. **Context visible** - Can the user see what this relates to without scrolling?
3. **Primary action clear** - Is it obvious which button to press?
4. **Escape route** - Is there a Cancel/Skip/Back option?
5. **Mobile-friendly** - DaisyUI handles responsive design, but check text isn't too long
6. **Smart default** - Is there a pre-selected sensible option?

## Real-World Example: Bug Triage Workflow

Agent needs to triage a reported bug:

**Step 1: Confirm it's a bug (not feature request)**
```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Classify Issue</h3>
    <p class="py-4">Issue #247: "Login button doesn't work on mobile Safari"</p>
    
    <div class="form-control">
      <label class="label cursor-pointer">
        <span class="label-text">🐛 Bug</span>
        <input type="radio" name="type" class="radio radio-primary" checked />
      </label>
      <label class="label cursor-pointer">
        <span class="label-text">✨ Feature Request</span>
        <input type="radio" name="type" class="radio radio-primary" />
      </label>
      <label class="label cursor-pointer">
        <span class="label-text">📖 Documentation</span>
        <input type="radio" name="type" class="radio radio-primary" />
      </label>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">Continue</button>
      <button class="btn">Skip</button>
    </div>
  </div>
</div>
```

**Step 2: Set severity**
```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Set Severity</h3>
    <p class="py-4">Bug: Login button doesn't work on mobile Safari</p>
    
    <select class="select select-bordered w-full">
      <option>Critical - System unusable</option>
      <option selected>High - Major feature broken</option>
      <option>Medium - Minor feature broken</option>
      <option>Low - Cosmetic issue</option>
    </select>
    
    <div class="modal-action">
      <button class="btn btn-primary">Set Severity</button>
      <button class="btn">Back</button>
    </div>
  </div>
</div>
```

**Step 3: Assign owner**
```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Assign Engineer</h3>
    <p class="py-4">High severity bug in authentication module</p>
    
    <select class="select select-bordered w-full">
      <option>Sarah Chen (Auth Team)</option>
      <option selected>Marcus Johnson (Auth Team)</option>
      <option>Unassigned</option>
    </select>
    <label class="label">
      <span class="label-text-alt">Marcus fixed similar Safari issues last week</span>
    </label>
    
    <div class="modal-action">
      <button class="btn btn-primary">Assign</button>
      <button class="btn">Leave Unassigned</button>
    </div>
  </div>
</div>
```

Each step focuses on one decision, shows context, and provides escape options.

## Tips for Agents

**When to create a component:**
- Anytime you need human input to proceed
- Before destructive actions
- When multiple valid options exist
- To confirm assumptions or preferences

**How to structure prompts to user:**
- Use natural language in titles
- Keep context sentences short (under 20 words)
- Pre-select smart defaults
- Put primary action first (left button)

**Theme support:**
Add `data-theme="light"` or `data-theme="dark"` to `<html>` tag. Available themes: light, dark, cupcake, bumblebee, emerald, corporate, synthwave, retro, cyberpunk, valentine, halloween, garden, forest, aqua, lofi, pastel, fantasy, wireframe, black, luxury, dracula, cmyk, autumn, business, acid, lemonade, night, coffee, winter, dim, nord, sunset.

**Accessibility:**
- Use semantic HTML
- Include proper labels
- Ensure keyboard navigation works (native HTML inputs)
- DaisyUI handles focus states automatically
