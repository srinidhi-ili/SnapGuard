document.addEventListener("DOMContentLoaded", function () {
    // Get dashboard elements
    const searchInput = document.getElementById("searchInput");
    const statusFilter = document.getElementById("statusFilter");
    const tableBody = document.getElementById("snapshotTableBody");

    // 1. SEARCH AND STATUS FILTER
    function filterSnapshots() {
        if (!tableBody) return;

        const rows = tableBody.querySelectorAll("tr");
        const searchText = searchInput
            ? searchInput.value.toLowerCase().trim()
            : "";

        const selectedStatus = statusFilter
            ? statusFilter.value.toLowerCase().trim()
            : "all";

        rows.forEach(function (row) {
            const rowText = row.textContent.toLowerCase();

            // Status is in the fifth column
            const statusCell = row.cells[4];
            const rowStatus = statusCell
                ? statusCell.textContent.toLowerCase().trim()
                : "";

            const matchesSearch = rowText.includes(searchText);
            const matchesStatus =
                selectedStatus === "" ||
                selectedStatus === "all" ||
                rowStatus.includes(selectedStatus);

            row.style.display =
                matchesSearch && matchesStatus ? "" : "none";
        });
    }

    if (searchInput) {
        searchInput.addEventListener("input", filterSnapshots);
    }

    if (statusFilter) {
        statusFilter.addEventListener("change", filterSnapshots);
    }

    // 2. SIDEBAR NAVIGATION
    // Navigation links should point to matching section IDs.
    document.querySelectorAll(".sidebar a[href^='#']").forEach(function (link) {
        link.addEventListener("click", function (event) {
            const targetId = link.getAttribute("href");
            const target = document.querySelector(targetId);

            if (target) {
                event.preventDefault();
                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        });
    });

    // 3. REFRESH BUTTON
    // Add data-action="refresh" to the refresh button.
    document.querySelectorAll('[data-action="refresh"]').forEach(function (button) {
        button.addEventListener("click", function () {
            if (searchInput) searchInput.value = "";
            if (statusFilter) statusFilter.value = "all";

            filterSnapshots();
            window.location.reload();
        });
    });

    // 4. SHOW A MESSAGE FOR PLACEHOLDER BUTTONS
    // Add data-message="Your message" to a button
    // when it should display a simple notification.
    document.querySelectorAll("[data-message]").forEach(function (button) {
        button.addEventListener("click", function () {
            alert(button.dataset.message);
        });
    });

    // Apply filters when the dashboard opens
    filterSnapshots();
});