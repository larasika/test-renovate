# test-renovate



## Current Behavior

When updating the version of a dependency using `rez` as package manager, the new version that Renovate provides doesn't match the precision of the existing version value.

Example : 

Current         | Update        |
-------------   | ------------- | 
pytest-3.6      | pytest-3.10.1 |

## Expected Behavior

When updating the version of a dependency using `rez` as package manager, the new version that Renovate provides should match the precision/pattern of the existing version value

Example : 

Current         | Update        |
-------------   | ------------- | 
pytest-3.6      | pytest-3.10   |
