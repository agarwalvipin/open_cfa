# CFA Reading Formatting Guide

## Overview
This guide provides a standardized formatting template for all CFA reading materials to ensure consistent, professional appearance with excellent on-screen readability and print quality.

## Reference Example
See `docs/LOS/FRA/Reading 33.md` for a complete implementation of these formatting standards.

---

## 1. Document Structure & Header Hierarchy

### Header Levels:
```markdown
## Reading XX: [Title]                    # Main reading title
### 🎯 Introduction                       # Introduction section
### Part X: [Topic] (LOS XX.x)           # Main parts with colored spans
#### X.X [Subtopic]                       # Major subsections
##### X.X.X [Detail]                      # Detailed sub-subsections
#### X.X Global & Local Context 🌍        # Context sections
```

### Numbering System:
- **Parts**: Use "Part 1", "Part 2", "Part 3" with colored spans
- **Subsections**: Use "1.1", "1.2", "1.3" (not "1.", "2.", "3.")
- **Sub-subsections**: Use "2.1.1", "2.1.2", "2.1.3"
- Include LOS references in Part headers: `(LOS XX.x)`
- Use horizontal rules (`-----`) to separate major Parts

---

## 2. Professional Color Scheme

### Header Colors (using HTML spans):

```markdown
### <span style="color: #1565C0;">Part X: [Title] (LOS XX.x)</span>
```

**Color Palette:**
- **Main Sections (Parts)**: `#1565C0` (Professional Navy Blue)
- **Subsections (X.1, X.2, etc.)**: `#6A1B9A` (Deep Purple)
- **Detail Subsections (X.1.1, X.1.2)**: `#E65100` (Deep Orange)
- **Context Sections**: `#00838F` (Professional Teal)

### Example Implementation:
```markdown
-----

### <span style="color: #1565C0;">Part 1: Topic Name (LOS 33.a)</span>

Introduction text for this part...

#### <span style="color: #6A1B9A;">1.1 Subsection Title</span>

Content here...

##### <span style="color: #E65100;">1.1.1 Detail Section</span>

More detailed content...

#### <span style="color: #00838F;">1.4 Global & Local Context 🌍</span>

Examples and context...

-----

### <span style="color: #1565C0;">Part 2: Next Topic (LOS 33.b)</span>
```

---

## 3. Callout Boxes

Replace all blockquotes (`> [!TIP]`, `> [!IMPORTANT]`) with styled div elements for better print quality.

### 💡 TIP Boxes (Light Blue):
```markdown
<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️:Your tip content here with **bold** text for emphasis.

</div>
</div>
```

### 💡 MNEMONIC Boxes (Light Purple):
```markdown
<div style="background-color: #F3E5F5; border-left: 5px solid #7B1FA2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 MNEMONIC: "[Memory Aid Title]"**
- **Point 1:** Details
- **Point 2:** Details
- Think: "Memory trick"

</div>
</div>
```

### 🎯 IMPORTANT Boxes (Soft Yellow):
```markdown
<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **Key Point 1:** 
  * **Sub-point** → **Action**
  * **IFRS:** Details
  * **U.S. GAAP:** Details
* **Key Point 2:** Content with ✅ YES or ❌ NO indicators
* **Impact Analysis:**
  * **Year 1:** ⬇️ Decreases X, Y, Z
  * **Future Years:** ⬆️ Increases A, B, C

</div>
</div>
```

**Styling Principles:**
- Always use `color: #000000; font-weight: 500;` for text inside divs (ensures dark print)
- Use visual indicators: ✅, ❌, ⬇️, ⬆️, → for better clarity
- Structure complex points with nested bullets
- Bold key terms for emphasis

---

## 4. Mathematical Formulas

Wrap all formulas in styled divs with light gray background:

### Single Formula:
```markdown
<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\text{Formula Name} = \text{Component 1} - \text{Component 2}$$

</div>
```

### Multiple Related Formulas:
```markdown
<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\text{Average Age} \approx \frac{\text{Accumulated Depreciation}}{\text{Annual Depreciation Expense}}$$

$$\text{Average Life} \approx \frac{\text{Ending Gross Investment}}{\text{Annual Depreciation Expense}}$$

$$\text{Remaining Life} \approx \frac{\text{Ending Net Investment}}{\text{Annual Depreciation Expense}}$$

</div>
```

### Formula Summary Section:
```markdown
### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Formula Name 1:** 

$$\text{Formula} = \text{Expression}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Formula Name 2:** 

$$\text{Formula} = \text{Expression}$$

</div>
```

**Formula Background:** `#F5F5F5` (Light gray) - subtle, professional, print-friendly

---

## 5. Bullet Point Indentation

Use consistent 2-space indentation for nested bullets:

```markdown
* **Main Point:**
  * Sub-point level 1
    * Sub-point level 2
      * Sub-point level 3
  * Another sub-point level 1
```

**Example:**
```markdown
* **Accounting:**
  * All identifiable intangible assets recorded at **fair value**
  * Any *excess* purchase price recorded as **Goodwill**
    
    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
    
    $$\text{Goodwill} = \text{Purchase Price} - \text{Fair Value of Net Assets}$$
    
    </div>
    
  * **Goodwill** is not amortized but tested for impairment annually
```

---

## 6. Complete Color Reference

### Header Colors:
| Element | Color Code | Color Name |
|---------|------------|------------|
| Main Parts | `#1565C0` | Professional Navy Blue |
| Subsections | `#6A1B9A` | Deep Purple |
| Detail Sections | `#E65100` | Deep Orange |
| Context Sections | `#00838F` | Professional Teal |

### Callout Box Colors:
| Box Type | Background | Border | Use Case |
|----------|------------|--------|----------|
| TIP | `#E3F2FD` | `#1976D2` | Exam tips, key insights |
| MNEMONIC | `#F3E5F5` | `#7B1FA2` | Memory aids, acronyms |
| IMPORTANT | `#FFF9E6` | `#F57C00` | Exam-day summary points |

### Formula Colors:
| Element | Color Code | Notes |
|---------|------------|-------|
| Formula Background | `#F5F5F5` | Light gray, print-friendly |

### Text Colors:
| Element | Color Code | Notes |
|---------|------------|-------|
| Callout Box Text | `#000000` | Black, ensures dark printing |

---

## 7. Step-by-Step Application Process

### For Each Reading:

1. **Update Header Hierarchy:**
   - Change numbered sections (1., 2., 3.) to proper headers (1.1, 1.2, 1.3)
   - Add color spans to headers according to the color scheme
   - Ensure proper nesting: Parts → Subsections → Details
   - Add horizontal rules (`-----`) between major Parts

2. **Convert Blockquotes to Styled Divs:**
   - Find all `> [!TIP]`, `> [!IMPORTANT]`, `> [!NOTE]`
   - Replace with appropriate styled div templates
   - Add black text color (`color: #000000; font-weight: 500;`)
   - Improve structure with nested bullets and visual indicators

3. **Add Formula Backgrounds:**
   - Wrap each formula in a light gray div
   - Group related formulas together when appropriate
   - Ensure proper spacing before and after formulas

4. **Fix Bullet Indentation:**
   - Use 2-space increments for nesting
   - Ensure consistent indentation throughout

5. **Enhance Important Boxes:**
   - Break down long sentences into structured bullet points
   - Bold key terms and concepts
   - Add arrows (→) for flow, emojis (✅❌⬇️⬆️) for visual clarity
   - Structure comparisons (IFRS vs U.S. GAAP) clearly

6. **Add Context Sections:**
   - Use teal color for "Global & Local Context" headers
   - Include relevant examples (global and local/Indian)

---

## 8. Quality Checklist

Before considering a reading complete, verify:

- [ ] All major Parts use colored span headers
- [ ] Horizontal rules (`-----`) separate major Parts
- [ ] All subsection headers use the correct color scheme
- [ ] All blockquotes converted to styled divs
- [ ] All formulas have light gray backgrounds
- [ ] All callout boxes have black text (`#000000`)
- [ ] Bullet indentation is consistent (2-space increments)
- [ ] Important concepts are **bolded**
- [ ] Visual indicators (✅❌→⬇️⬆️) used where appropriate
- [ ] Formula Summary section properly formatted
- [ ] Print preview shows dark, readable text (not light gray)
- [ ] Color scheme is balanced and professional throughout

---

## 9. Example Transformation

### BEFORE:
```markdown
### Part 1: Topic Name

**1. First Section**

> [!TIP]
> Remember: Key point here.

* Formula: $$X = Y + Z$$
```

### AFTER:
```markdown
-----

### <span style="color: #1565C0;">Part 1: Topic Name (LOS XX.a)</span>

Brief introduction to this part...

#### <span style="color: #6A1B9A;">1.1 First Section</span>

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️:Remember: **Key point** here with proper **emphasis**.

</div>
</div>

* **Formula Explanation:**
  
  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
  
  $$X = Y + Z$$
  
  </div>

-----
```

---

## 10. Reference Files

**Primary Reference:** `docs/LOS/FRA/Reading 33.md`

This file demonstrates:
- Complete header hierarchy with colors
- All three types of callout boxes (TIP, MNEMONIC, IMPORTANT)
- Formula backgrounds in context and summary sections
- Proper bullet indentation
- Professional color scheme throughout
- Excellent print quality

**This Guide:** `/home/vipin/projects/open_cfa/FORMATTING_GUIDE.md`

---

## Notes

- All colors chosen for professional appearance and print quality
- Light backgrounds ensure formulas and callouts stand out without heavy ink usage
- Black text (`#000000`) in all styled divs ensures readability when printed
- Rounded corners (`border-radius: 5px`) provide modern, polished look
- Consistent spacing and padding creates breathing room for better readability
- Color-coded headers create clear visual hierarchy for navigation

Apply these standards consistently across all readings for a professional, cohesive study resource.
