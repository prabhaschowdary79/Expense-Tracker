document.addEventListener('DOMContentLoaded', () => {
    const expenses = [];
    const expenseForm = document.getElementById('expense-form');
    const expensesTable = document.getElementById('expenses-table');
    const themeButtons = document.querySelectorAll('.theme-btn');
    const loginForm = document.getElementById('login-form');
    const loginScreen = document.getElementById('login-screen');
    const expenseTracker = document.getElementById('expense-tracker');
    const loginError = document.getElementById('login-error');

    // Theme toggling
    themeButtons.forEach(button => {
        button.addEventListener('click', () => {
            document.body.className = button.dataset.theme;
        });
    });

    // Hardcoded credentials
    const hardcodedUsername = 'user';
    const hardcodedPassword = 'password123';

    // Add Expense
    const addExpense = (event) => {
        event.preventDefault();

        const amount = parseFloat(document.getElementById('amount').value);
        const category = document.getElementById('category').value;
        const description = document.getElementById('description').value;
        const date = document.getElementById('date').value;

        if (!amount || !category || !description || !date) {
            alert('Please fill out all fields!');
            return;
        }

        const expense = { amount, category, description, date };
        expenses.push(expense);
        renderExpenses();
        renderCharts(); // Re-render charts after adding an expense

        expenseForm.reset();
    };

    // Render Expenses
    const renderExpenses = () => {
        expensesTable.innerHTML = '';
        expenses.forEach((expense, index) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${expense.date}</td>
                <td>${expense.category}</td>
                <td>₹${expense.amount.toFixed(2)}</td>
                <td>${expense.description}</td>
                <td class="actions">
                    <button class="edit" onclick="editExpense(${index})">Edit</button>
                    <button class="delete" onclick="deleteExpense(${index})">Delete</button>
                </td>
            `;
            expensesTable.appendChild(row);
        });
    };

    // Edit Expense
    const editExpense = (index) => {
        const expense = expenses[index];
        document.getElementById('amount').value = expense.amount;
        document.getElementById('category').value = expense.category;
        document.getElementById('description').value = expense.description;
        document.getElementById('date').value = expense.date;
        deleteExpense(index);
    };

    // Delete Expense
    const deleteExpense = (index) => {
        expenses.splice(index, 1);
        renderExpenses();
        renderCharts(); // Re-render charts after deleting an expense
    };

    // Render Charts (Pie and Bar)
    const renderCharts = () => {
        // Pie Chart for Category-wise Expenses
        const categoryChart = document.getElementById('category-pie-chart').getContext('2d');
        const categories = [...new Set(expenses.map(expense => expense.category))];
        const categoryData = categories.map(category => 
            expenses.filter(expense => expense.category === category).reduce((sum, expense) => sum + expense.amount, 0)
        );

        new Chart(categoryChart, {
            type: 'pie',
            data: {
                labels: categories,
                datasets: [{
                    data: categoryData,
                    backgroundColor: ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1'],
                    borderColor: '#fff',
                    borderWidth: 2,
                }]
            }
        });

        // Monthly Bar Chart
        const monthlyChart = document.getElementById('monthly-bar-chart').getContext('2d');
        const monthlyData = Array(12).fill(0);
        expenses.forEach(expense => {
            const month = new Date(expense.date).getMonth();
            monthlyData[month] += expense.amount;
        });

        new Chart(monthlyChart, {
            type: 'bar',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                datasets: [{
                    label: 'Expenses (₹)',
                    data: monthlyData,
                    backgroundColor: '#ffb3b3',
                    borderColor: '#ff6666',
                    borderWidth: 1
                }]
            }
        });

        // Yearly Bar Chart
        const yearlyChart = document.getElementById('yearly-bar-chart').getContext('2d');
        const yearlyData = [];
        expenses.forEach(expense => {
            const year = new Date(expense.date).getFullYear();
            const index = yearlyData.findIndex(data => data.year === year);
            if (index === -1) {
                yearlyData.push({ year, total: expense.amount });
            } else {
                yearlyData[index].total += expense.amount;
            }
        });

        new Chart(yearlyChart, {
            type: 'bar',
            data: {
                labels: yearlyData.map(data => data.year),
                datasets: [{
                    label: 'Expenses (₹)',
                    data: yearlyData.map(data => data.total),
                    backgroundColor: '#88c9e6',
                    borderColor: '#5bc0de',
                    borderWidth: 1
                }]
            }
        });
    };

    // Handle Login
    loginForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (username === hardcodedUsername && password === hardcodedPassword) {
            loginScreen.style.display = 'none';
            expenseTracker.style.display = 'block';
        } else {
            loginError.style.display = 'block';
        }
    });

    // Attach add expense event
    expenseForm.addEventListener('submit', addExpense);
});




