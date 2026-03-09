# --- STEP 1: LOAD PACKAGES ---
# We need ggplot2 for plotting and ggprism for scientific styling
library(ggplot2)
library(ggprism)
library(dplyr) # Useful for data manipulation

# --- STEP 2: CREATE MOCK DATA ---
# This simulates a simple proteomics results table
# log2FC = Log2 Fold Change (Difference in abundance)
# p_val = Statistical significance
proteomics_data <- data.frame(
  Protein_ID = c("Albumin", "Keratin", "Tubulin", "Actin", "Myosin", "Casein", "Insulin", "Hsp70", "GAPDH", "P53"),
  log2FC = c(0.1, 4.5, -0.2, -3.8, 0.05, 5.2, -4.1, 1.2, -0.1, 2.5),
  p_val = c(0.85, 0.001, 0.65, 0.0005, 0.92, 0.0001, 0.002, 0.04, 0.78, 0.03)
)

# --- STEP 3: DATA PROCESSING ---
# We need to categorize proteins.
# Rule: If p_val < 0.05 AND absolute log2FC > 1, it is "Significant". Otherwise "Not Significant".

processed_data <- proteomics_data %>%
  mutate(
    # calculate -log10 p-value for the Y-axis of the volcano plot
    neg_log10_p = -log10(p_val),
    
    # Create a grouping column for coloring
    # HINT: Use ifelse() to check the conditions
    Category = ifelse(p_val < 0.05 & abs(log2FC) > 1, "Significant", "Not Significant")
  )

# --- STEP 4: PLOTTING ---
# Fill in the aesthetics to map the data to the axes

volcano_plot <- ggplot(processed_data, aes(x = log2FC, y = neg_log10_p, color = Category)) +
  
  # Add the geometric object for a scatter plot
  geom_point(size = 3, alpha = 0.8) + 
  
  # Manually set colors: Grey for Not Sig, Red for Significant
  scale_color_manual(values = c("Not Significant" = "grey", "Significant" = "red")) +
  
  # Add labels
  labs(
    title = "Differential Expression: Drug vs Control",
    x = "Log2 Fold Change",
    y = "-Log10 P-value"
  ) +
  
  # --- STEP 5: APPLY THEME ---
  # Use ggprism to give it a 'GraphPad Prism' look
  theme_prism(base_size = 14)

# Display the plot
print(volcano_plot)