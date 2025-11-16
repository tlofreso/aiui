# DaisyUI Chat Card Patterns

This document contains reference patterns and examples for generating chat cards using DaisyUI components.

## Core Design Principles

- Cards are designed to be displayed inline within a chat application
- Use compact sizing (`btn-xs`, `text-xs`, `text-sm`) for space efficiency
- Cards are centered with `flex justify-center`
- Maximum width is typically `max-w-sm` for readability
- Use `bg-base-200` or `bg-base-100` with borders for backgrounds
- All cards include shadow (`shadow-md`) for visual separation

## Card Pattern Categories

### 1. Affirmative/Negative Response Cards

Used when confirmation or yes/no decision is needed.

**Structure:**
- Card title describing the action
- Question text
- Two action buttons (typically "No" and "Yes")
- Use `btn-error` for negative action, `btn-primary` for affirmative

**Example:**
```html
<div class="flex justify-center">
    <div class="card bg-base-200 w-full max-w-sm shadow-md">
        <div class="card-body p-4">
            <h2 class="card-title text-sm">Confirm Action</h2>
            <p class="text-xs">Would you like me to send this email to all team members?</p>
            <div class="card-actions justify-end gap-2">
                <button class="btn btn-error btn-xs">No</button>
                <button class="btn btn-primary btn-xs">Yes, Send</button>
            </div>
        </div>
    </div>
</div>
```

### 2. Multiple Choice (Radio) Cards

Used when user needs to select one option from several choices.

**Structure:**
- Card title describing the choice
- Optional description text
- Radio input list with labels
- Single confirm button
- Each option uses `radio radio-xs` class
- Use `cursor-pointer` on labels for better UX

**Example:**
```html
<div class="flex justify-center">
    <div class="card bg-base-200 w-full max-w-sm shadow-md">
        <div class="card-body p-4">
            <h2 class="card-title text-sm">Choose a Response Style</h2>
            <p class="text-xs mb-2">How would you like me to respond?</p>
            <ul class="text-xs space-y-1">
                <li>
                    <label class="cursor-pointer flex items-center gap-2">
                        <input type="radio" name="response-style" class="radio radio-xs" checked />
                        <span>Concise and brief</span>
                    </label>
                </li>
                <li>
                    <label class="cursor-pointer flex items-center gap-2">
                        <input type="radio" name="response-style" class="radio radio-xs" />
                        <span>Detailed explanation</span>
                    </label>
                </li>
                <li>
                    <label class="cursor-pointer flex items-center gap-2">
                        <input type="radio" name="response-style" class="radio radio-xs" />
                        <span>Step-by-step guide</span>
                    </label>
                </li>
            </ul>
            <div class="card-actions justify-end mt-2">
                <button class="btn btn-primary btn-xs">Confirm</button>
            </div>
        </div>
    </div>
</div>
```

### 3. Multiple Select (Checkbox) Cards

Used when user can select multiple options from a list.

**Structure:**
- Card title describing the selection
- Optional description text
- Checkbox list with labels
- Single action button
- Each option uses `checkbox checkbox-xs` class
- Use `cursor-pointer` on labels

**Example:**
```html
<div class="flex justify-center">
    <div class="card bg-base-200 w-full max-w-sm shadow-md">
        <div class="card-body p-4">
            <h2 class="card-title text-sm">Select Topics to Include</h2>
            <p class="text-xs mb-2">Which sections should I include in the report?</p>
            <ul class="text-xs space-y-1">
                <li>
                    <label class="cursor-pointer flex items-center gap-2">
                        <input type="checkbox" class="checkbox checkbox-xs" checked />
                        <span>Executive Summary</span>
                    </label>
                </li>
                <li>
                    <label class="cursor-pointer flex items-center gap-2">
                        <input type="checkbox" class="checkbox checkbox-xs" checked />
                        <span>Financial Analysis</span>
                    </label>
                </li>
                <li>
                    <label class="cursor-pointer flex items-center gap-2">
                        <input type="checkbox" class="checkbox checkbox-xs" />
                        <span>Market Research</span>
                    </label>
                </li>
                <li>
                    <label class="cursor-pointer flex items-center gap-2">
                        <input type="checkbox" class="checkbox checkbox-xs" checked />
                        <span>Recommendations</span>
                    </label>
                </li>
            </ul>
            <div class="card-actions justify-end mt-2">
                <button class="btn btn-primary btn-xs">Generate Report</button>
            </div>
        </div>
    </div>
</div>
```

### 4. Content Preview with Feedback Cards

Used to show drafted content (email, message, document) with options to revise or approve.

**Structure:**
- Card title indicating content type
- Content preview area with `bg-base-200` background
- Textarea for feedback input
- Multiple action buttons (typically "Revise" and primary action)
- Use `btn-ghost` for secondary actions

**Example:**
```html
<div class="flex justify-center">
    <div class="card bg-base-100 border border-base-300 w-full max-w-sm shadow-md">
        <div class="card-body p-4">
            <h2 class="card-title text-sm">Email Draft</h2>
            <div class="bg-base-200 p-3 rounded text-xs mb-3">
                <div class="mb-2">
                    <strong>To:</strong> team@company.com<br/>
                    <strong>Subject:</strong> Q4 Planning Meeting
                </div>
                <div class="text-xs opacity-80">
                    Hi Team,<br/><br/>
                    I hope this message finds you well. I wanted to schedule our Q4 planning meeting for next week. Please review the attached agenda and let me know your availability.<br/><br/>
                    Best regards
                </div>
            </div>
            <textarea
                class="textarea textarea-bordered textarea-sm w-full text-xs"
                placeholder="Provide feedback or request changes..."
                rows="2"></textarea>
            <div class="card-actions justify-end mt-2 gap-2">
                <button class="btn btn-ghost btn-xs">Revise</button>
                <button class="btn btn-primary btn-xs">Send Draft</button>
            </div>
        </div>
    </div>
</div>
```

## DaisyUI Component Reference

### Common Classes

**Card Structure:**
- `card` - Base card component
- `card-body` - Card content wrapper (use `p-4` for compact padding)
- `card-title` - Card title (use with `text-sm`)
- `card-actions` - Action button container (typically `justify-end`)

**Buttons:**
- `btn` - Base button
- `btn-xs` - Extra small size (recommended for chat cards)
- `btn-primary` - Primary action style
- `btn-error` - Destructive action style
- `btn-ghost` - Subtle secondary action style

**Form Elements:**
- `radio radio-xs` - Radio button (extra small)
- `checkbox checkbox-xs` - Checkbox (extra small)
- `textarea textarea-bordered textarea-sm` - Text area with border and small size

**Backgrounds:**
- `bg-base-100` - Lightest base color
- `bg-base-200` - Slightly darker base color
- `bg-base-300` - Even darker base color

**Utility:**
- `shadow-md` - Medium shadow
- `rounded` - Rounded corners
- `gap-2` - Gap spacing between elements
- `space-y-1` - Vertical spacing between list items
- `opacity-80` - 80% opacity

## Best Practices

1. **Consistency**: Use the same size classes (`btn-xs`, `text-xs`, `text-sm`) throughout a card
2. **Hierarchy**: Card titles should be `text-sm`, body text `text-xs`
3. **Actions**: Place primary actions on the right, secondary/destructive on the left
4. **Spacing**: Use `p-4` for card body, `gap-2` for button spacing, `space-y-1` for list items
5. **Accessibility**: Always include descriptive labels and proper input names
6. **Readability**: Keep content concise for inline chat display
7. **Visual Weight**: Use borders (`border border-base-300`) for lighter backgrounds (`bg-base-100`)
