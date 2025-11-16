# Advanced Patterns

Additional patterns for complex interaction scenarios.

## Multi-Step Wizard

When you need to collect related information across multiple screens:

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box max-w-2xl">
      <!-- Progress indicator -->
      <ul class="steps w-full mb-6">
        <li class="step step-primary">Type</li>
        <li class="step step-primary">Details</li>
        <li class="step">Review</li>
      </ul>
      
      <!-- Current step content -->
      <h3 class="font-bold text-lg">Add Description</h3>
      <p class="py-4">Provide details about the new feature request</p>
      
      <textarea 
        class="textarea textarea-bordered w-full h-32" 
        placeholder="Describe what the feature should do..."
      ></textarea>
      
      <!-- Navigation -->
      <div class="modal-action">
        <button class="btn">Back</button>
        <button class="btn btn-primary">Next</button>
      </div>
    </div>
  </div>
</body>
</html>
```

**Guidelines for multi-step:**
- Use `steps` component to show progress
- Always show current step number (e.g., "Step 2 of 3")
- Include both Back and Next buttons (except first/last step)
- Each step should be completable in <30 seconds
- Maximum 3-4 steps total

## Loading States

Show progress while waiting for agent actions:

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Analyzing Code</h3>
    <p class="py-4">Scanning 247 files for security vulnerabilities...</p>
    
    <!-- Progress bar -->
    <progress class="progress progress-primary w-full" value="70" max="100"></progress>
    <p class="text-sm text-gray-500 mt-2">70% complete</p>
    
    <!-- Loading spinner alternative -->
    <!-- <span class="loading loading-spinner loading-lg"></span> -->
    
    <div class="modal-action">
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

**Loading states:**
- `loading loading-spinner` - Spinning circle
- `loading loading-dots` - Three animated dots
- `loading loading-ring` - Ring spinner
- `loading loading-ball` - Bouncing ball
- `progress` - Determinate progress bar

Sizes: `loading-xs`, `loading-sm`, `loading-md`, `loading-lg`

## Inline Validation

Provide immediate feedback on user input:

```html
<div class="form-control w-full max-w-xs">
  <label class="label">
    <span class="label-text">Repository Name</span>
  </label>
  <input 
    type="text" 
    placeholder="my-awesome-project"
    class="input input-bordered input-success w-full max-w-xs" 
  />
  <label class="label">
    <span class="label-text-alt text-success">✓ Available</span>
  </label>
</div>
```

**Validation states:**
- `input-success` + green text - Valid input
- `input-error` + red text - Invalid input
- `input-warning` + yellow text - Warning/caution

**Error example:**
```html
<input 
  type="text" 
  class="input input-bordered input-error w-full max-w-xs" 
/>
<label class="label">
  <span class="label-text-alt text-error">
    ✗ Name must be lowercase and contain only letters, numbers, and hyphens
  </span>
</label>
```

## Conditional Display

Show/hide options based on previous selections:

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Configure Deployment</h3>
    
    <!-- Primary choice -->
    <div class="form-control">
      <label class="label cursor-pointer">
        <span class="label-text">Automatic deployment</span>
        <input type="radio" name="deploy" class="radio radio-primary" checked />
      </label>
      <label class="label cursor-pointer">
        <span class="label-text">Manual approval required</span>
        <input type="radio" name="deploy" class="radio radio-primary" />
      </label>
    </div>
    
    <!-- Conditional section (shown only for manual approval) -->
    <div class="mt-4 p-4 bg-base-200 rounded-lg">
      <p class="text-sm font-semibold mb-2">Approval Settings</p>
      <select class="select select-bordered select-sm w-full">
        <option>Any team member</option>
        <option>Tech lead only</option>
        <option>Two approvals required</option>
      </select>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">Save</button>
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

Use `bg-base-200 rounded-lg` to visually nest conditional options.

## Date and Time Selection

For scheduling and deadline setting:

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Schedule Deployment</h3>
    <p class="py-4">When should we deploy to production?</p>
    
    <div class="grid grid-cols-2 gap-4">
      <div class="form-control">
        <label class="label">
          <span class="label-text">Date</span>
        </label>
        <input 
          type="date" 
          class="input input-bordered w-full"
          value="2025-11-15"
        />
      </div>
      
      <div class="form-control">
        <label class="label">
          <span class="label-text">Time (UTC)</span>
        </label>
        <input 
          type="time" 
          class="input input-bordered w-full"
          value="02:00"
        />
      </div>
    </div>
    
    <div class="alert alert-info mt-4">
      <span>Scheduled for off-peak hours (2 AM UTC)</span>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">Schedule</button>
      <button class="btn">Deploy Now</button>
    </div>
  </div>
</div>
```

**Quick time options:**
```html
<div class="btn-group">
  <button class="btn btn-sm">30 min</button>
  <button class="btn btn-sm btn-active">1 hour</button>
  <button class="btn btn-sm">2 hours</button>
  <button class="btn btn-sm">Tomorrow</button>
</div>
```

## File Upload

For attaching files or selecting resources:

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Upload Configuration</h3>
    <p class="py-4">Select the .env file for deployment</p>
    
    <input 
      type="file" 
      class="file-input file-input-bordered w-full" 
      accept=".env"
    />
    
    <div class="alert alert-warning mt-4">
      <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
      </svg>
      <span>Ensure no sensitive data is exposed in the file</span>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">Upload</button>
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

**File input variants:**
- `file-input-primary` - Primary color
- `file-input-secondary` - Secondary color
- `file-input-sm` - Small size
- `file-input-lg` - Large size

## Badge and Tag Display

Show status, counts, or categories:

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Review Changes</h3>
    <p class="py-4">Pull Request #42: Add user authentication</p>
    
    <div class="flex gap-2 mb-4">
      <div class="badge badge-success">3 approvals</div>
      <div class="badge badge-warning">2 pending checks</div>
      <div class="badge badge-ghost">12 files changed</div>
    </div>
    
    <div class="space-y-2">
      <div class="flex items-center gap-2">
        <div class="badge badge-sm">frontend</div>
        <span class="text-sm">Updated login form</span>
      </div>
      <div class="flex items-center gap-2">
        <div class="badge badge-sm">backend</div>
        <span class="text-sm">Added JWT middleware</span>
      </div>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">Merge</button>
      <button class="btn">Close</button>
    </div>
  </div>
</div>
```

**Badge variants:**
- `badge-primary`, `badge-secondary` - Colored
- `badge-success`, `badge-warning`, `badge-error` - Status
- `badge-ghost`, `badge-outline` - Subtle
- `badge-lg`, `badge-md`, `badge-sm`, `badge-xs` - Sizes

## Toast Notifications

For non-blocking feedback that doesn't interrupt flow:

```html
<div class="toast toast-top toast-end">
  <div class="alert alert-success">
    <span>File saved successfully!</span>
  </div>
</div>
```

**Toast positions:**
- `toast-top` / `toast-bottom` - Vertical
- `toast-start` / `toast-center` / `toast-end` - Horizontal
- Combine: `toast-top toast-end` (top-right corner)

**Common patterns:**
```html
<!-- Success -->
<div class="toast toast-top toast-end">
  <div class="alert alert-success">
    <span>✓ Changes committed</span>
  </div>
</div>

<!-- Error -->
<div class="toast toast-bottom">
  <div class="alert alert-error">
    <span>✗ Build failed - check logs</span>
  </div>
</div>

<!-- Info -->
<div class="toast toast-top">
  <div class="alert alert-info">
    <span>ℹ Deployment queued (3 ahead of you)</span>
  </div>
</div>
```

## Collapsible Details

Show additional information on demand:

```html
<div class="modal modal-open">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Deploy to Production</h3>
    <p class="py-4">Ready to deploy v2.1.3</p>
    
    <!-- Main action -->
    <div class="alert alert-success">
      <span>All tests passed ✓</span>
    </div>
    
    <!-- Optional details -->
    <div class="collapse collapse-arrow bg-base-200 mt-4">
      <input type="checkbox" />
      <div class="collapse-title text-sm font-medium">
        View deployment details
      </div>
      <div class="collapse-content text-sm">
        <ul class="list-disc list-inside space-y-1">
          <li>Docker image: myapp:v2.1.3</li>
          <li>Replicas: 3</li>
          <li>Region: us-east-1</li>
          <li>Estimated time: 5 minutes</li>
        </ul>
      </div>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">Deploy</button>
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

## Table Selection

When choosing from structured data:

```html
<div class="modal modal-open">
  <div class="modal-box max-w-3xl">
    <h3 class="font-bold text-lg">Select Database</h3>
    <p class="py-4">Which database should we use for user data?</p>
    
    <div class="overflow-x-auto">
      <table class="table">
        <thead>
          <tr>
            <th></th>
            <th>Database</th>
            <th>Type</th>
            <th>Status</th>
            <th>Size</th>
          </tr>
        </thead>
        <tbody>
          <tr class="hover">
            <td><input type="radio" name="db" class="radio radio-primary" /></td>
            <td>users-prod</td>
            <td><div class="badge badge-sm">PostgreSQL</div></td>
            <td><div class="badge badge-success badge-sm">Active</div></td>
            <td>2.3 GB</td>
          </tr>
          <tr class="hover">
            <td><input type="radio" name="db" class="radio radio-primary" checked /></td>
            <td>users-staging</td>
            <td><div class="badge badge-sm">PostgreSQL</div></td>
            <td><div class="badge badge-success badge-sm">Active</div></td>
            <td>847 MB</td>
          </tr>
          <tr class="hover">
            <td><input type="radio" name="db" class="radio radio-primary" /></td>
            <td>users-archive</td>
            <td><div class="badge badge-sm">PostgreSQL</div></td>
            <td><div class="badge badge-ghost badge-sm">Inactive</div></td>
            <td>15.7 GB</td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">Select</button>
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

**Table utilities:**
- `table-zebra` - Alternating row colors
- `table-sm` - Compact size
- `hover` - Row hover effect
- `overflow-x-auto` - Horizontal scroll wrapper

## Timeline Display

Show sequential events or history:

```html
<div class="card w-96 bg-base-100 shadow-xl">
  <div class="card-body">
    <h2 class="card-title">Deployment History</h2>
    
    <ul class="timeline timeline-vertical">
      <li>
        <div class="timeline-start">10:30 AM</div>
        <div class="timeline-middle">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" />
          </svg>
        </div>
        <div class="timeline-end timeline-box">Tests passed</div>
        <hr class="bg-primary"/>
      </li>
      <li>
        <hr class="bg-primary"/>
        <div class="timeline-start">10:32 AM</div>
        <div class="timeline-middle">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" />
          </svg>
        </div>
        <div class="timeline-end timeline-box">Build complete</div>
        <hr class="bg-primary"/>
      </li>
      <li>
        <hr class="bg-primary"/>
        <div class="timeline-start">10:35 AM</div>
        <div class="timeline-middle">
          <div class="loading loading-spinner loading-sm"></div>
        </div>
        <div class="timeline-end timeline-box">Deploying...</div>
      </li>
    </ul>
    
    <div class="card-actions justify-end mt-4">
      <button class="btn btn-sm">View Logs</button>
    </div>
  </div>
</div>
```

## Tabs for Related Options

Organize choices into categories:

```html
<div class="modal modal-open">
  <div class="modal-box max-w-2xl">
    <h3 class="font-bold text-lg">Select Environment</h3>
    
    <div role="tablist" class="tabs tabs-boxed">
      <a role="tab" class="tab">Development</a>
      <a role="tab" class="tab tab-active">Staging</a>
      <a role="tab" class="tab">Production</a>
    </div>
    
    <!-- Staging tab content -->
    <div class="py-4">
      <div class="alert alert-info">
        <span>Staging environment - safe for testing</span>
      </div>
      
      <div class="form-control mt-4">
        <label class="label">
          <span class="label-text">Server</span>
        </label>
        <select class="select select-bordered w-full">
          <option>staging-01.example.com</option>
          <option selected>staging-02.example.com</option>
        </select>
      </div>
    </div>
    
    <div class="modal-action">
      <button class="btn btn-primary">Deploy to Staging</button>
      <button class="btn">Cancel</button>
    </div>
  </div>
</div>
```

**Tab variants:**
- `tabs-boxed` - Boxed style
- `tabs-bordered` - With border
- `tabs-lifted` - Lifted tab style
- `tabs-lg`, `tabs-md`, `tabs-sm`, `tabs-xs` - Sizes

## When to Use Advanced Patterns

**Multi-step wizard**: Related information that doesn't fit one screen (3-4 steps max)

**Loading states**: Any operation taking >2 seconds

**Inline validation**: Forms with specific format requirements

**Conditional display**: Options that depend on previous choices

**Date/time**: Scheduling, deadlines, time-based configurations

**File upload**: Importing configs, attachments, resource selection

**Badges**: Status indicators, counts, categories, tags

**Toast**: Background confirmations, non-critical alerts

**Collapsible**: Nice-to-know info that's not essential

**Table selection**: Choosing from structured data with multiple attributes

**Timeline**: Event history, deployment steps, audit logs

**Tabs**: Grouping related options by category (don't overuse)
