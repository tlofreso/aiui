# Ready-to-Use Templates

Complete HTML templates you can copy and customize immediately.

## Template Structure

All templates follow this base structure:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Feedback UI</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <!-- Component goes here -->
</body>
</html>
```

## Quick Decision Modal

For simple yes/no or choice between 2-3 options:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quick Decision</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Proceed with Deployment?</h3>
      <p class="py-4">
        This will deploy <strong>v2.1.3</strong> to production. 
        All tests have passed and staging looks good.
      </p>
      
      <div class="modal-action">
        <button class="btn btn-primary">Yes, Deploy</button>
        <button class="btn">No, Cancel</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Replace title text
- Update context in `<p>`
- Change button labels

## Priority Selection

For choosing priority, severity, or importance level:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Set Priority</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Set Task Priority</h3>
      <p class="py-4">Task: <strong>Implement user authentication</strong></p>
      
      <div class="form-control">
        <label class="label cursor-pointer">
          <span class="label-text">🔴 Critical - Blocking release</span>
          <input type="radio" name="priority" class="radio radio-error" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">🟠 High - Should complete this sprint</span>
          <input type="radio" name="priority" class="radio radio-warning" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">🟡 Medium - Complete when possible</span>
          <input type="radio" name="priority" class="radio radio-primary" checked />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">🟢 Low - Nice to have</span>
          <input type="radio" name="priority" class="radio radio-success" />
        </label>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-primary">Set Priority</button>
        <button class="btn">Cancel</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Change task name
- Modify priority options
- Adjust which option is `checked`
- Change emoji indicators

## Text Input with Helper

For collecting names, titles, or short descriptions:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Text Input</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Name Your Branch</h3>
      <p class="py-4">Creating a new branch for: User authentication feature</p>
      
      <div class="form-control">
        <label class="label">
          <span class="label-text">Branch Name</span>
        </label>
        <input 
          type="text" 
          placeholder="feature/user-auth" 
          class="input input-bordered w-full"
          value="feature/user-authentication"
        />
        <label class="label">
          <span class="label-text-alt">Use lowercase with hyphens (e.g., feature/my-feature)</span>
        </label>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-primary">Create Branch</button>
        <button class="btn">Cancel</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Change title and context
- Update placeholder and default value
- Modify helper text

## Confirmation with Warning

For destructive or irreversible actions:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Confirm Action</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">⚠️ Delete Database Backup?</h3>
      <p class="py-4">
        You are about to delete backup <strong>"users-db-2025-11-01.sql"</strong> 
        which is <strong>2.3 GB</strong>.
      </p>
      
      <div class="alert alert-warning">
        <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
        </svg>
        <span>This action cannot be undone. The backup will be permanently deleted.</span>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-error">Delete Permanently</button>
        <button class="btn">Cancel</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Update item being deleted
- Change warning message
- Adjust button text (keep "Delete" or similar clear)

## Dropdown Selection

For choosing from a predefined list:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Select Option</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Select Deployment Strategy</h3>
      <p class="py-4">For release <strong>v2.1.3</strong> to production</p>
      
      <div class="form-control">
        <label class="label">
          <span class="label-text">Strategy</span>
        </label>
        <select class="select select-bordered w-full">
          <option>Rolling Update - Deploy gradually across servers</option>
          <option selected>Blue-Green - Switch all traffic at once</option>
          <option>Canary - Test with 10% of users first</option>
        </select>
        <label class="label">
          <span class="label-text-alt">Recommended: Blue-Green for major releases</span>
        </label>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-primary">Deploy</button>
        <button class="btn">Cancel</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Change selection options
- Update context and recommendation
- Modify which option is `selected`

## Multi-line Text Input

For descriptions, comments, or longer feedback:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Add Description</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Explain Priority Increase</h3>
      <p class="py-4">
        Why should we increase priority of 
        <strong>"Fix mobile Safari login bug"</strong>?
      </p>
      
      <textarea 
        class="textarea textarea-bordered w-full h-32" 
        placeholder="Describe the impact or urgency..."
      >Affecting 15% of mobile users. Customer complaints increasing. Blocks new user signups on iOS devices.</textarea>
      
      <label class="label">
        <span class="label-text-alt">Optional: Add any relevant context</span>
      </label>
      
      <div class="modal-action">
        <button class="btn btn-primary">Submit</button>
        <button class="btn">Skip</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Change question/prompt
- Update placeholder or default text
- Adjust textarea height (`h-24`, `h-32`, `h-48`)

## Multiple Choice Selection

For selecting multiple items from a list:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Multiple Selection</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Select Affected Systems</h3>
      <p class="py-4">Which systems need to be restarted after the update?</p>
      
      <div class="form-control">
        <label class="label cursor-pointer">
          <span class="label-text">Web Servers (nginx)</span>
          <input type="checkbox" checked class="checkbox checkbox-primary" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">API Servers (Node.js)</span>
          <input type="checkbox" checked class="checkbox checkbox-primary" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">Background Workers</span>
          <input type="checkbox" class="checkbox checkbox-primary" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">Database (PostgreSQL)</span>
          <input type="checkbox" class="checkbox checkbox-primary" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">Cache (Redis)</span>
          <input type="checkbox" class="checkbox checkbox-primary" />
        </label>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-primary">Restart Selected</button>
        <button class="btn">Cancel</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Change options list
- Update which items are `checked` by default
- Modify context

## Success Confirmation

To show successful completion:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Success</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <div class="alert alert-success">
        <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span>Successfully deployed to production!</span>
      </div>
      
      <div class="py-4 space-y-2">
        <p><strong>Version:</strong> v2.1.3</p>
        <p><strong>Deployed to:</strong> production (all regions)</p>
        <p><strong>URL:</strong> <a href="https://app.example.com" class="link link-primary">https://app.example.com</a></p>
        <p><strong>Deployment time:</strong> 2m 34s</p>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-primary">View App</button>
        <button class="btn">Close</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Update success message
- Change details shown
- Modify button actions

## Numeric Input

For setting quantities, timeouts, or numeric values:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Set Value</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Set Request Timeout</h3>
      <p class="py-4">How long should we wait for API responses?</p>
      
      <div class="form-control">
        <label class="label">
          <span class="label-text">Timeout (seconds)</span>
        </label>
        <input 
          type="number" 
          value="30" 
          min="5" 
          max="300"
          class="input input-bordered w-full max-w-xs" 
        />
        <label class="label">
          <span class="label-text-alt">Range: 5-300 seconds. Recommended: 30 seconds</span>
        </label>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-primary">Set Timeout</button>
        <button class="btn">Use Default (30s)</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Change value name and context
- Update default value, min, max
- Modify helper text

## Loading Progress

To show an operation in progress:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Loading</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Running Tests</h3>
      <p class="py-4">Executing 247 test cases...</p>
      
      <progress class="progress progress-primary w-full" value="70" max="100"></progress>
      <p class="text-sm text-gray-500 mt-2">173 of 247 tests complete (70%)</p>
      
      <div class="alert alert-info mt-4">
        <span>Current: Integration tests for authentication module</span>
      </div>
      
      <div class="modal-action">
        <button class="btn">Cancel Tests</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Change operation description
- Update progress value and max
- Modify status message

## Card-Style Choice

Alternative to modal for less intrusive prompts:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Card Choice</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="flex items-center justify-center min-h-screen bg-base-200">
  <div class="card w-96 bg-base-100 shadow-xl">
    <div class="card-body">
      <h2 class="card-title">Merge Pull Request?</h2>
      <p>PR #42: Add user authentication module</p>
      
      <div class="flex gap-2 my-2">
        <div class="badge badge-success">All checks passed</div>
        <div class="badge badge-info">2 approvals</div>
      </div>
      
      <div class="card-actions justify-end">
        <button class="btn btn-ghost">Close</button>
        <button class="btn btn-primary">Merge</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Customize:**
- Change title and description
- Update badges
- Modify button labels

## Usage Tips

**Choosing templates:**
1. **Quick Decision** - Binary choice or 2-3 options
2. **Priority Selection** - When options have clear hierarchy
3. **Text Input** - Short text like names or IDs
4. **Confirmation with Warning** - Destructive or irreversible actions
5. **Dropdown** - 4+ predefined options
6. **Multi-line Text** - Descriptions or explanations
7. **Multiple Choice** - When multiple selections are valid
8. **Success** - Confirm operation completed
9. **Numeric Input** - Quantities or thresholds
10. **Loading** - Show progress for long operations
11. **Card-Style** - Less intrusive than modal

**Customization checklist:**
- [ ] Replace title text
- [ ] Update context paragraph
- [ ] Change input options/values
- [ ] Adjust smart defaults (checked/selected)
- [ ] Modify button labels
- [ ] Update helper text

**Testing:**
- Open HTML file in browser
- Verify text makes sense
- Check buttons are clear
- Ensure context is complete
- Test on mobile (resize browser)

**Next steps after customization:**
1. Save to `.html` file
2. Test in browser
3. Integrate with your agent workflow
4. Capture user responses via form handling
