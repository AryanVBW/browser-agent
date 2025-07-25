# Pull Request

## Description

<!-- Provide a brief description of the changes in this PR -->

### Type of Change

<!-- Mark the relevant option with an "x" -->

- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📚 Documentation update
- [ ] 🔧 Configuration change
- [ ] 🧪 Test improvement
- [ ] ♻️ Code refactoring (no functional changes)
- [ ] ⚡ Performance improvement
- [ ] 🔒 Security improvement
- [ ] 🎨 UI/UX improvement
- [ ] 🔨 Build/CI improvement
- [ ] 📦 Dependency update
- [ ] 🧹 Code cleanup
- [ ] 🌐 Internationalization
- [ ] ♿ Accessibility improvement

## Related Issues

<!-- Link to related issues using keywords like "Fixes", "Closes", "Resolves" -->
<!-- Example: Fixes #123, Closes #456 -->

- Fixes #
- Closes #
- Related to #

## Changes Made

<!-- Describe the changes in detail -->

### Core Changes

- 
- 
- 

### Files Modified

<!-- List the main files that were changed -->

- `path/to/file1.py` - Description of changes
- `path/to/file2.py` - Description of changes
- `path/to/file3.py` - Description of changes

### New Files Added

<!-- List any new files that were added -->

- `path/to/new_file1.py` - Purpose and description
- `path/to/new_file2.py` - Purpose and description

### Files Removed

<!-- List any files that were removed -->

- `path/to/removed_file.py` - Reason for removal

## Testing

### Test Coverage

<!-- Describe how you tested your changes -->

- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] End-to-end tests added/updated
- [ ] Manual testing performed
- [ ] Browser compatibility tested
- [ ] Performance testing done
- [ ] Security testing done

### Test Results

<!-- Provide test results or screenshots -->

```bash
# Test command and results
$ make test
# Paste test output here
```

### Manual Testing Steps

<!-- Describe the steps to manually test the changes -->

1. 
2. 
3. 
4. 

### Test Environment

- **OS**: 
- **Python Version**: 
- **Browser**: 
- **Browser Driver**: 
- **Dependencies**: 

## Screenshots/Videos

<!-- Add screenshots or videos to demonstrate the changes (if applicable) -->

### Before

<!-- Screenshot or description of behavior before changes -->

### After

<!-- Screenshot or description of behavior after changes -->

## Performance Impact

<!-- Describe any performance implications -->

- [ ] No performance impact
- [ ] Performance improvement (describe below)
- [ ] Potential performance regression (describe below and justify)
- [ ] Performance impact unknown/needs testing

### Performance Details

<!-- If there's a performance impact, provide details -->

- **Benchmark results**: 
- **Memory usage**: 
- **CPU usage**: 
- **Network impact**: 
- **Startup time**: 

## Breaking Changes

<!-- Describe any breaking changes and migration path -->

- [ ] No breaking changes
- [ ] Breaking changes (describe below)

### Breaking Change Details

<!-- If there are breaking changes, provide details -->

#### What breaks:

- 
- 

#### Migration path:

1. 
2. 
3. 

#### Deprecation timeline:

- **Deprecated in**: v
- **Removed in**: v

## Dependencies

### New Dependencies

<!-- List any new dependencies added -->

- `package-name==version` - Purpose and justification
- `another-package>=version` - Purpose and justification

### Updated Dependencies

<!-- List any dependencies that were updated -->

- `package-name`: `old-version` → `new-version` - Reason for update
- `another-package`: `old-version` → `new-version` - Reason for update

### Removed Dependencies

<!-- List any dependencies that were removed -->

- `package-name` - Reason for removal

## Configuration Changes

<!-- Describe any configuration changes -->

- [ ] No configuration changes
- [ ] New configuration options added
- [ ] Existing configuration options modified
- [ ] Configuration options removed

### Configuration Details

<!-- If there are configuration changes, provide details -->

#### New options:

```yaml
# Example configuration
new_option:
  enabled: true
  value: "default"
```

#### Modified options:

- `option_name`: Changed from X to Y
- `another_option`: New default value

#### Removed options:

- `old_option`: No longer needed because...

## Documentation

<!-- Describe documentation changes -->

- [ ] Documentation updated
- [ ] New documentation added
- [ ] API documentation updated
- [ ] README updated
- [ ] CHANGELOG updated
- [ ] Examples updated
- [ ] No documentation changes needed

### Documentation Changes

<!-- List specific documentation changes -->

- Updated `docs/section.md` to reflect new feature
- Added example in `examples/new_feature.py`
- Updated API reference for `ClassName.method_name`

## Security Considerations

<!-- Describe any security implications -->

- [ ] No security implications
- [ ] Security improvement
- [ ] Potential security impact (describe below)
- [ ] Security review needed

### Security Details

<!-- If there are security implications, provide details -->

- **Vulnerability fixed**: 
- **New security features**: 
- **Potential risks**: 
- **Mitigation strategies**: 

## Backward Compatibility

<!-- Describe backward compatibility -->

- [ ] Fully backward compatible
- [ ] Backward compatible with deprecation warnings
- [ ] Not backward compatible (breaking changes documented above)

## Deployment Notes

<!-- Any special deployment considerations -->

- [ ] No special deployment requirements
- [ ] Database migration required
- [ ] Configuration update required
- [ ] Service restart required
- [ ] Special deployment steps (describe below)

### Deployment Steps

<!-- If special deployment steps are needed -->

1. 
2. 
3. 

## Checklist

### Code Quality

- [ ] Code follows the project's style guidelines
- [ ] Self-review of code completed
- [ ] Code is well-commented and documented
- [ ] No debugging code or console logs left
- [ ] Error handling is appropriate
- [ ] Code is efficient and follows best practices

### Testing

- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Test coverage is adequate (>80%)
- [ ] Edge cases are tested
- [ ] Error conditions are tested
- [ ] Performance tests added (if applicable)

### Documentation

- [ ] Code is self-documenting with clear variable/function names
- [ ] Docstrings added for new functions/classes
- [ ] Type hints added where appropriate
- [ ] README updated (if applicable)
- [ ] API documentation updated (if applicable)
- [ ] Examples updated (if applicable)

### Dependencies

- [ ] New dependencies are justified and minimal
- [ ] Dependency versions are pinned appropriately
- [ ] License compatibility checked for new dependencies
- [ ] Security vulnerabilities checked in dependencies

### Git

- [ ] Commit messages are clear and descriptive
- [ ] Commits are logically organized
- [ ] No merge commits in feature branch
- [ ] Branch is up to date with main/master
- [ ] No sensitive information in commit history

### CI/CD

- [ ] All CI checks pass
- [ ] Build succeeds on all target platforms
- [ ] Linting passes
- [ ] Type checking passes
- [ ] Security scans pass

## Additional Notes

<!-- Any additional information for reviewers -->

### Review Focus Areas

<!-- Highlight areas that need special attention during review -->

- 
- 
- 

### Known Issues

<!-- List any known issues or limitations -->

- 
- 

### Future Work

<!-- Describe any follow-up work that should be done -->

- 
- 

### Questions for Reviewers

<!-- Ask specific questions to guide the review -->

- 
- 

---

## For Maintainers

### Release Notes

<!-- Suggested content for release notes -->

```markdown
### Added
- 

### Changed
- 

### Fixed
- 

### Deprecated
- 

### Removed
- 

### Security
- 
```

### Merge Checklist

- [ ] PR title follows conventional commit format
- [ ] All required reviews completed
- [ ] All CI checks pass
- [ ] Documentation is complete and accurate
- [ ] Breaking changes are properly documented
- [ ] Release notes are prepared
- [ ] Milestone assigned (if applicable)
- [ ] Labels assigned appropriately