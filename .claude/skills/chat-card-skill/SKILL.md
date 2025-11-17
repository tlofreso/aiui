---
name: chat-card-skill
description: Generate inline chat cards using DaisyUI components for user interactions. Use when creating interactive UI elements within a chat interface that require user input, confirmation, or selection. Supports affirmative/negative responses, multiple choice (radio), multiple select (checkbox), and content preview with feedback patterns.
---

# Chat Card Skill

This skill provides patterns and guidance for generating HTML cards using DaisyUI components that display inline within chat applications.

## Purpose

Generate interactive, visually consistent chat cards for common user interaction patterns including confirmations, selections, and content previews. Cards are optimized for inline display in chat interfaces with compact sizing and clear action flows.

## When to Use This Skill

Use this skill when:
- Creating confirmation dialogs or yes/no prompts within chat
- Presenting multiple choice questions to users
- Allowing users to select multiple options from a list
- Displaying drafted content (emails, messages, documents) for review and feedback
- Any scenario requiring interactive UI elements inline with chat messages

## Card Pattern Types

### 1. Affirmative/Negative Response Cards
For binary decisions or confirmations. Include a title, question text, and two action buttons (negative and affirmative).

### 2. Multiple Choice (Radio) Cards
For single-selection from multiple options. Include a title, optional description, radio button list, and confirmation button.

### 3. Multiple Select (Checkbox) Cards
For multi-selection from a list. Include a title, optional description, checkbox list, and action button.

### 4. Content Preview with Feedback Cards
For displaying drafted content with revision options. Include a title, content preview area, feedback textarea, and action buttons.

## Implementation Guidelines

### Sizing and Layout
- Use compact sizing throughout: `btn-xs` for buttons, `text-xs` for body text, `text-sm` for titles
- Center cards with `flex justify-center`
- Set maximum width to `max-w-sm` for readability
- Apply `shadow-md` to all cards for visual separation
- Use `p-4` for card body padding

### Color Scheme
- Card backgrounds: `bg-base-200` or `bg-base-100` with `border border-base-300`
- Primary actions: `btn-primary`
- Destructive/negative actions: `btn-error`
- Secondary actions: `btn-ghost`
- Content preview areas: `bg-base-200` with `rounded`

### Action Button Placement
- Use `card-actions justify-end` to right-align buttons
- Place primary action on the right
- Place secondary/destructive actions on the left
- Use `gap-2` for spacing between buttons

### Form Elements
- Radio buttons: `radio radio-xs` class
- Checkboxes: `checkbox checkbox-xs` class
- Text areas: `textarea textarea-bordered textarea-sm`
- Use `cursor-pointer` on labels for better UX
- Use `space-y-1` for vertical spacing in lists

### Content Structure
Each card should follow this structure:
1. Outer container: `<div class="flex justify-center">`
2. Card wrapper: `<div class="card bg-base-200 w-full max-w-sm shadow-md">`
3. Card body: `<div class="card-body p-4">`
4. Title: `<h2 class="card-title text-sm">`
5. Content area (text, form elements, preview)
6. Actions: `<div class="card-actions justify-end [mt-2/mt-3] gap-2">`

## Detailed Reference

For complete examples and detailed pattern documentation, refer to `references/card-patterns.md` which includes:
- Full HTML examples for each card type
- DaisyUI component reference
- Best practices and accessibility guidelines
- Visual hierarchy and spacing recommendations

## Customization

Adapt card patterns based on context:
- Adjust button text to match specific actions
- Modify option lists based on user needs
- Customize preview content structure for different content types
- Add or remove form elements as needed while maintaining visual consistency

## Output Format

Generate complete, self-contained HTML snippets that can be directly inserted into a chat application. Ensure all necessary DaisyUI classes are included and properly structured.

## CRITICAL: Required Data Attributes

ALL interactive cards MUST include these data attributes for functionality:

**1. Card Element:**
- `data-card-type="[type]"` - Required on the card div
- Values: "affirmative-negative", "multiple-choice", "multiple-select", or "content-preview"

**2. Form Element:**
- `data-card-form` - Required wrapper for form-based cards (all except affirmative-negative)
- Use `<form data-card-form>` to wrap card content

**3. Buttons:**
- `data-card-action="[action]"` - Required on EVERY button
- Values: "yes", "no", "submit", "skip", "send", "revise", etc.

**4. Form Inputs:**
- `name` attribute - Required for all inputs (radio, checkbox, textarea)
- `value` attribute - Required for radio buttons and checkboxes

**Without these attributes, the cards will not be interactive.** Always refer to the exact patterns in `references/card-patterns.md` - do not improvise or create custom structures.
