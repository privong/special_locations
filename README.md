# Special Locations

Use [magellan](https://github.com/privong/magellan) GPS logging data to characterize the movements of a user.
This includes the identification of commonly visited locations, typical departure times from said locations, and common routes taken.

## Classification Targets

### Locations

- home
- work
- favorite locations (restaurant, bar, gym, etc.)

### Transit Information

- departure from home/work
- typical routes taken
    - daily commuting
    - common trips

## Implementation

Use a bayesian framework to establish the initial identification of those locations and to generate new priors for looking for updates (e.g., moving house, changing jobs, etc.).
