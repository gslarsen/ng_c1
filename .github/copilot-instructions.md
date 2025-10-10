# Copilot Instructions for ng_c1

## Project Overview
This is a **machine learning course lab repository** containing Jupyter notebooks and Python utilities for Andrew Ng's Machine Learning Specialization (Course 1). The codebase is structured around weekly modules focusing on linear regression concepts, from univariate to multivariate implementations.

## Architecture & Structure

### Week-Based Organization
- `w1-intro-to-ml/`: Univariate linear regression - model representation, cost functions, gradient descent
- `w2-multiple-linear-regression/`: Multivariate regression - feature scaling, polynomial regression, scikit-learn integration
- `env/`: Python virtual environment (ignored in version control)
- `betaversion/` folders: Contains earlier versions of labs

### Core Components
1. **Jupyter Notebooks** (`C1_W*_Lab*.ipynb`): Self-contained tutorial notebooks with markdown explanations and executable code cells
2. **Utility Modules**:
   - `lab_utils_common.py`: Shared cost/gradient computation functions (both loop and vectorized implementations)
   - `lab_utils_uni.py`: Univariate plotting routines (cost visualization, gradient descent animation)
   - `lab_utils_multi.py`: Multivariate utilities (3D plots, contour plots, data loading)
3. **Data Files**: CSV format (`data.txt`, `data/ex1data2.txt`)
4. **Styling**: `deeplearning.mplstyle` - custom matplotlib configuration with specific color scheme

## Key Patterns & Conventions

### Naming Conventions
- **Partial derivatives**: Follow pattern `dj_dw` for ∂J/∂w, `dj_db` for ∂J/∂b
- **Model functions**: `f_wb` represents f(w,b) predictions
- **Parameters**: `w` (weights), `b` (bias), `alpha` (learning rate)
- **Data**: `X_train` (features matrix), `y_train` (target values)
- Notebooks use `_Soln` suffix indicating solution versions

### Code Patterns
```python
# Dual implementations - both loop and vectorized (matrix) versions exist:
compute_cost()        # Loop version for clarity
compute_cost_matrix() # Vectorized version for performance

# Standard gradient descent signature:
gradient_descent(x, y, w_in, b_in, alpha, num_iters, cost_function, gradient_function)

# Data shape conventions:
# X: (m, n) where m=examples, n=features
# y: (m,) target vector
# w: (n,) weight vector
```

### Visualization Standards
- Use custom color palette: `dlblue='#0096ff'`, `dlorange='#FF9300'`, `dldarkred='#C00000'`, `dlmagenta='#FF40FF'`, `dlpurple='#7030A0'`
- Always apply `plt.style.use('./deeplearning.mplstyle')` before plotting
- Import plotting functions from `lab_utils_*` modules rather than reimplementing

### Data Loading
```python
# Week 1: Simple text files
data = np.loadtxt("data.txt", delimiter=',')

# Week 2: Use provided loader
from lab_utils_multi import load_house_data
X_train, y_train = load_house_data()  # Loads from data/ex1data2.txt
```

## Development Workflow

### Environment Setup
This project uses a Python virtual environment in `env/`:
```bash
source env/bin/activate  # Activate before running notebooks
```

Required packages (inferred from imports):
- numpy, matplotlib, scipy
- scikit-learn (Week 2 labs)
- ipywidgets (for interactive visualizations)
- jupyter/ipykernel

### Running Notebooks
- Execute cells sequentially - notebooks build on previous cells
- Each notebook is self-contained with its own imports and data setup
- Plotting requires `deeplearning.mplstyle` in the same directory

### Code Organization
- Utility functions are **duplicated** across week folders (each week is self-contained)
- `lab_utils_common.py` provides both educational (loop-based) and efficient (vectorized) implementations
- Interactive widgets use `@interact` decorator from ipywidgets

## Machine Learning Context

### Mathematical Notation Mapping
```
Python Variable → Math Symbol → Meaning
X               → 𝐗           → Feature matrix
y               → 𝐲           → Target vector
w               → 𝐰           → Weight parameters
b               → b           → Bias parameter
m               → m           → Number of examples
n               → n           → Number of features
alpha           → α           → Learning rate
```

### Implementation Philosophy
- **Educational clarity over efficiency**: Loop versions provided alongside vectorized implementations
- **Gradual complexity**: Week 1 uses scalars, Week 2 introduces vectors/matrices
- **Visualization-heavy**: Extensive plotting to illustrate cost surfaces, gradient descent paths

## Testing & Validation
- No formal test suite - validation done through notebook execution
- Visual inspection of plots is primary validation method
- Notebooks include expected output values in markdown for manual verification

## Integration Points
- **Scikit-learn integration** (Week 2): Uses `SGDRegressor` and `StandardScaler`
- **Data format**: CSV files with comma delimiters, no headers
- **No external APIs** or services - fully local execution

## Common Tasks

### Adding New Lab Content
1. Create notebook following naming convention: `C1_W{week}_Lab{number}_{topic}_Soln.ipynb`
2. Import from local `lab_utils_*` modules (assume same directory)
3. Include Goals/Tools/Notation sections in opening markdown cells
4. Apply `plt.style.use('./deeplearning.mplstyle')` for consistency

### Modifying Utility Functions
- Update in **both week folders** if the function is shared
- Maintain dual implementations (loop + vectorized) where they exist
- Preserve function signatures to avoid breaking notebooks

### Working with Data
- Keep data files in week directories or `data/` subdirectories
- Use relative paths from notebook location (e.g., `"./data.txt"` or `"data/ex1data2.txt"`)
- Maintain CSV format with comma delimiters
