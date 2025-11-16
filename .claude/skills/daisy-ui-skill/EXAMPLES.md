# Real-World Workflow Examples

Complete workflows showing how multiple components work together.

## Workflow 1: Bug Triage

Agent receives a bug report and needs to triage it through multiple steps.

### Step 1: Classify the Issue

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Classify Issue</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <div class="badge badge-ghost mb-4">Step 1 of 3</div>
      
      <h3 class="font-bold text-lg">Classify Issue</h3>
      <p class="py-4">
        <strong>Issue #247:</strong> "Login button doesn't respond when clicked on mobile Safari"
      </p>
      
      <div class="form-control">
        <label class="label cursor-pointer">
          <span class="label-text">🐛 Bug - Something isn't working</span>
          <input type="radio" name="type" class="radio radio-primary" checked />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">✨ Feature Request - New functionality</span>
          <input type="radio" name="type" class="radio radio-primary" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">📖 Documentation - Needs better docs</span>
          <input type="radio" name="type" class="radio radio-primary" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">❓ Question - Needs clarification</span>
          <input type="radio" name="type" class="radio radio-primary" />
        </label>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-primary">Continue →</button>
        <button class="btn">Skip Triage</button>
      </div>
    </div>
  </div>
</body>
</html>
```

### Step 2: Set Priority/Severity

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
      <div class="badge badge-ghost mb-4">Step 2 of 3</div>
      
      <h3 class="font-bold text-lg">Set Bug Severity</h3>
      <p class="py-4">
        <strong>Bug:</strong> Login button doesn't respond on mobile Safari
      </p>
      
      <div class="alert alert-info mb-4">
        <span>Affects: iOS Safari users trying to log in</span>
      </div>
      
      <select class="select select-bordered w-full">
        <option>🔴 Critical - System down, no workaround</option>
        <option selected>🟠 High - Major feature broken</option>
        <option>🟡 Medium - Feature impaired, workaround exists</option>
        <option>🟢 Low - Minor issue, cosmetic</option>
      </select>
      
      <label class="label">
        <span class="label-text-alt">
          Recommended: High - Login is critical functionality
        </span>
      </label>
      
      <div class="modal-action">
        <button class="btn">← Back</button>
        <button class="btn btn-primary">Continue →</button>
      </div>
    </div>
  </div>
</body>
</html>
```

### Step 3: Assign Engineer

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Assign Engineer</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <div class="badge badge-ghost mb-4">Step 3 of 3</div>
      
      <h3 class="font-bold text-lg">Assign to Engineer</h3>
      <p class="py-4">
        High severity bug in <strong>authentication module</strong>
      </p>
      
      <div class="flex gap-2 mb-4">
        <div class="badge badge-error">High Priority</div>
        <div class="badge badge-ghost">Mobile Safari</div>
        <div class="badge badge-ghost">Login</div>
      </div>
      
      <select class="select select-bordered w-full">
        <option>Sarah Chen - Authentication Team</option>
        <option selected>Marcus Johnson - Authentication Team</option>
        <option>Elena Rodriguez - Frontend Team</option>
        <option>Leave Unassigned</option>
      </select>
      
      <label class="label">
        <span class="label-text-alt">
          ℹ️ Marcus fixed similar Safari issues in PR #234
        </span>
      </label>
      
      <div class="modal-action">
        <button class="btn">← Back</button>
        <button class="btn btn-primary">Complete Triage</button>
      </div>
    </div>
  </div>
</body>
</html>
```

### Step 4: Confirmation

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Triage Complete</title>
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
        <span>Bug successfully triaged!</span>
      </div>
      
      <div class="py-4 space-y-2">
        <p><strong>Issue:</strong> #247</p>
        <p><strong>Type:</strong> Bug</p>
        <p><strong>Severity:</strong> High</p>
        <p><strong>Assigned to:</strong> Marcus Johnson</p>
      </div>
      
      <div class="alert alert-info">
        <span>Notification sent to Marcus Johnson</span>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-primary">View Issue</button>
        <button class="btn">Close</button>
      </div>
    </div>
  </div>
</body>
</html>
```

## Workflow 2: Code Review Approval

Agent completes code analysis and needs human approval to proceed.

### Step 1: Show Analysis Results

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Review Results</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box max-w-2xl">
      <h3 class="font-bold text-lg">Code Review Complete</h3>
      <p class="py-4">Analysis of PR #42: "Add JWT authentication"</p>
      
      <div class="stats stats-vertical lg:stats-horizontal shadow w-full">
        <div class="stat">
          <div class="stat-title">Files Changed</div>
          <div class="stat-value text-primary">12</div>
        </div>
        <div class="stat">
          <div class="stat-title">Lines Added</div>
          <div class="stat-value text-success">+247</div>
        </div>
        <div class="stat">
          <div class="stat-title">Lines Removed</div>
          <div class="stat-value text-error">-43</div>
        </div>
      </div>
      
      <div class="mt-4 space-y-2">
        <div class="alert alert-success">
          <span>✓ All tests passing (127/127)</span>
        </div>
        <div class="alert alert-success">
          <span>✓ No security vulnerabilities found</span>
        </div>
        <div class="alert alert-warning">
          <span>⚠️ Code coverage decreased by 2% (needs additional tests)</span>
        </div>
      </div>
      
      <div class="collapse collapse-arrow bg-base-200 mt-4">
        <input type="checkbox" />
        <div class="collapse-title text-sm font-medium">
          View detailed findings (3 items)
        </div>
        <div class="collapse-content text-sm">
          <ul class="list-disc list-inside space-y-1">
            <li>auth/jwt.ts: Consider adding rate limiting to token generation</li>
            <li>middleware/auth.ts: Missing error handling for expired tokens</li>
            <li>tests/: Add integration tests for token refresh flow</li>
          </ul>
        </div>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-primary">Approve & Merge</button>
        <button class="btn btn-warning">Request Changes</button>
        <button class="btn">Close</button>
      </div>
    </div>
  </div>
</body>
</html>
```

### Step 2: Request Changes (if selected)

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Request Changes</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Request Changes</h3>
      <p class="py-4">What changes are needed before approval?</p>
      
      <div class="form-control mb-4">
        <label class="label cursor-pointer">
          <span class="label-text">Add missing integration tests</span>
          <input type="checkbox" checked class="checkbox checkbox-primary" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">Improve error handling for expired tokens</span>
          <input type="checkbox" checked class="checkbox checkbox-primary" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">Add rate limiting to token generation</span>
          <input type="checkbox" class="checkbox checkbox-primary" />
        </label>
      </div>
      
      <textarea 
        class="textarea textarea-bordered w-full h-24" 
        placeholder="Additional comments (optional)..."
      ></textarea>
      
      <div class="modal-action">
        <button class="btn">← Back</button>
        <button class="btn btn-primary">Submit Feedback</button>
      </div>
    </div>
  </div>
</body>
</html>
```

## Workflow 3: Deployment Configuration

Agent needs configuration choices before deploying.

### Step 1: Choose Environment

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Select Environment</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Deploy Application</h3>
      <p class="py-4">Version <strong>v2.1.3</strong> is ready to deploy</p>
      
      <div class="form-control">
        <label class="label cursor-pointer">
          <div>
            <span class="label-text font-semibold">Development</span>
            <p class="text-xs text-gray-500">For testing new features</p>
          </div>
          <input type="radio" name="env" class="radio radio-primary" />
        </label>
        
        <label class="label cursor-pointer">
          <div>
            <span class="label-text font-semibold">Staging</span>
            <p class="text-xs text-gray-500">Pre-production testing environment</p>
          </div>
          <input type="radio" name="env" class="radio radio-primary" checked />
        </label>
        
        <label class="label cursor-pointer">
          <div>
            <span class="label-text font-semibold">Production</span>
            <p class="text-xs text-gray-500">Live environment (requires approval)</p>
          </div>
          <input type="radio" name="env" class="radio radio-primary" />
        </label>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-primary">Continue →</button>
        <button class="btn">Cancel</button>
      </div>
    </div>
  </div>
</body>
</html>
```

### Step 2: Deployment Strategy (for production)

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Deployment Strategy</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Select Deployment Strategy</h3>
      <p class="py-4">How should we deploy to production?</p>
      
      <div class="space-y-3">
        <div class="card bg-base-200 hover:bg-base-300 cursor-pointer">
          <div class="card-body p-4">
            <div class="flex items-start gap-3">
              <input type="radio" name="strategy" class="radio radio-primary mt-1" checked />
              <div>
                <h4 class="font-semibold">Blue-Green Deployment</h4>
                <p class="text-sm text-gray-600">
                  Deploy to new environment, then switch traffic all at once
                </p>
                <div class="badge badge-sm mt-2">Recommended</div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="card bg-base-200 hover:bg-base-300 cursor-pointer">
          <div class="card-body p-4">
            <div class="flex items-start gap-3">
              <input type="radio" name="strategy" class="radio radio-primary mt-1" />
              <div>
                <h4 class="font-semibold">Rolling Update</h4>
                <p class="text-sm text-gray-600">
                  Gradually update servers one at a time
                </p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="card bg-base-200 hover:bg-base-300 cursor-pointer">
          <div class="card-body p-4">
            <div class="flex items-start gap-3">
              <input type="radio" name="strategy" class="radio radio-primary mt-1" />
              <div>
                <h4 class="font-semibold">Canary Deployment</h4>
                <p class="text-sm text-gray-600">
                  Deploy to 10% of users first, then gradually increase
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="modal-action">
        <button class="btn">← Back</button>
        <button class="btn btn-primary">Continue →</button>
      </div>
    </div>
  </div>
</body>
</html>
```

### Step 3: Schedule Deployment

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Schedule Deployment</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">When to Deploy?</h3>
      <p class="py-4">Production deployment with Blue-Green strategy</p>
      
      <div class="form-control mb-4">
        <label class="label cursor-pointer">
          <span class="label-text">Deploy Now</span>
          <input type="radio" name="when" class="radio radio-primary" />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">Schedule for Later</span>
          <input type="radio" name="when" class="radio radio-primary" checked />
        </label>
      </div>
      
      <!-- Shown when "Schedule for Later" is selected -->
      <div class="grid grid-cols-2 gap-4 p-4 bg-base-200 rounded-lg">
        <div class="form-control">
          <label class="label">
            <span class="label-text text-sm">Date</span>
          </label>
          <input 
            type="date" 
            class="input input-bordered input-sm w-full"
            value="2025-11-15"
          />
        </div>
        
        <div class="form-control">
          <label class="label">
            <span class="label-text text-sm">Time (UTC)</span>
          </label>
          <input 
            type="time" 
            class="input input-bordered input-sm w-full"
            value="02:00"
          />
        </div>
      </div>
      
      <div class="alert alert-info mt-4">
        <span>ℹ️ Scheduled for off-peak hours (2 AM UTC)</span>
      </div>
      
      <div class="modal-action">
        <button class="btn">← Back</button>
        <button class="btn btn-primary">Schedule Deployment</button>
      </div>
    </div>
  </div>
</body>
</html>
```

### Step 4: Deployment Progress

```html
<!DOCTYPE html>
<html data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Deploying</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Deploying to Production</h3>
      
      <ul class="timeline timeline-vertical mt-6">
        <li>
          <div class="timeline-start text-xs">10:32</div>
          <div class="timeline-middle">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5 text-success">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" />
            </svg>
          </div>
          <div class="timeline-end timeline-box">Build complete</div>
          <hr class="bg-success"/>
        </li>
        
        <li>
          <hr class="bg-success"/>
          <div class="timeline-start text-xs">10:35</div>
          <div class="timeline-middle">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5 text-success">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" />
            </svg>
          </div>
          <div class="timeline-end timeline-box">Tests passed</div>
          <hr class="bg-success"/>
        </li>
        
        <li>
          <hr class="bg-success"/>
          <div class="timeline-start text-xs">10:38</div>
          <div class="timeline-middle">
            <div class="loading loading-spinner loading-sm text-primary"></div>
          </div>
          <div class="timeline-end timeline-box">Deploying to blue environment...</div>
          <hr />
        </li>
        
        <li>
          <hr />
          <div class="timeline-start text-xs">--:--</div>
          <div class="timeline-middle">
            <div class="w-5 h-5 rounded-full border-2 border-gray-300"></div>
          </div>
          <div class="timeline-end timeline-box text-gray-400">Switch traffic</div>
          <hr />
        </li>
        
        <li>
          <hr />
          <div class="timeline-start text-xs">--:--</div>
          <div class="timeline-middle">
            <div class="w-5 h-5 rounded-full border-2 border-gray-300"></div>
          </div>
          <div class="timeline-end timeline-box text-gray-400">Verify deployment</div>
        </li>
      </ul>
      
      <div class="alert alert-info mt-6">
        <span>Estimated time remaining: 2 minutes</span>
      </div>
      
      <div class="modal-action">
        <button class="btn btn-error btn-outline">Cancel Deployment</button>
      </div>
    </div>
  </div>
</body>
</html>
```

## Pattern Notes

**Multi-step workflows:**
- Show progress indicator (Step X of Y, or timeline)
- Include Back button (except first step)
- Show context from previous steps
- Keep each step focused on one decision

**Conditional flows:**
- Use visual nesting (bg-base-200 rounded-lg) for dependent options
- Only show relevant options based on previous selections
- Provide defaults that make sense for the path chosen

**Progress indication:**
- Use timeline for sequential steps
- Use progress bar for quantifiable tasks
- Use spinner for indeterminate operations
- Always show what's happening ("Deploying...", not just loading)

**Contextual information:**
- Show key details from conversation
- Use badges to highlight important attributes
- Provide recommendations when helpful
- Include escape hatches ("Leave Unassigned", "Deploy Now")
