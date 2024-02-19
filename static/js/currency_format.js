function formatCurrency(value) {
    return `<span class="float-end">${value.toLocaleString('en-US', { minimumFractionDigits: 0 })}</span>`;
}

export { formatCurrency };