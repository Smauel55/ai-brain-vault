---
created: 2026-05-12
updated: 2026-05-12
tags: [learning, claude-code, day-1, model-vs-harness]
---

# Day 1 — Model vs. Harness

## In my own words

So basically a model is like the overarching system that is the foundation for all the Specific Ai's to work off of. It is like the framework off of which you can build custom AI's to do a variety of things, but it alone cannot do much at all. A harness is like a connector that connects the Model to a tool or series of tools that allows it to become useful in certain capacities.

## What Claude flagged after

- The harness definition is solid: harness wraps the model and gives it tools.
- The model definition has one slip worth fixing: the model is not a "framework you build custom AIs on top of." The model IS the AI. It's a single trained system that takes text in and produces text out. Multiple harnesses can wrap the same model, but the model itself is the singular brain, not the foundation underneath many brains.
- More precise version: "the model is the actual AI doing the thinking, but it can only read and write text. A harness is what gives the model hands — tools to read files, run commands, browse the web — and turns it from a text generator into something that can act."

## Why it matters

When something feels off about Claude, the first question is: model problem or harness problem? They have different fixes. A model problem means I need to prompt better. A harness problem means I need to change a setting, command, or workflow.

## Triage — model problem or harness problem

### Signals it's a MODEL problem
- Claude is confidently wrong about a fact, function, URL, or date
- Claude misunderstood and answered a different question
- Output is repetitive, off-topic, or weirdly long
- Same prompt twice gave noticeably different answers
- Claude wrote correct-looking code or instructions that do not actually work
- Claude contradicts itself within one response
- Bad reasoning: arithmetic errors, logic gaps, jumped to a conclusion

In all of these, the model produced a response. The response is just wrong, lazy, or off.

### Signals it's a HARNESS problem
- Claude said "I do not have access to that" / "I can not do that" / "I do not have a tool for..."
- An error message mentions a tool, file path, command, permission, or settings file
- Claude asked permission to run something
- A slash command returned an error or did not behave as expected
- Memory did not carry forward to a new session
- A file got written to the wrong place, or not at all
- A previously-working workflow stopped working with no prompt change
- Output got truncated mid-sentence with a note about length

In all of these, the model did not actually try to do the thing, or tried and the harness blocked, lost, or mangled the result.

### 30-second triage flow
1. **Did Claude refuse, error, or say "I can't"?** → Harness problem. Missing tool or permission.
2. **Did Claude do the thing, but the result is wrong/weird/wrong-shaped?** → Model problem. Reprompt with specifics, examples, constraints.
3. **Did Claude say it did the thing, but you can not tell if it actually did?** → Verification problem. Check the artifact yourself. Open the file. Run the thing.

### The one trap
Sometimes a model problem **looks like** a harness problem. Example: Claude says "I tried to read the file but it does not exist" when the file does exist, because Claude looked in the wrong place. That is a model problem dressed up as harness. Tell: harness errors mention paths, tools, permissions specifically. Model confusion is vaguer.
