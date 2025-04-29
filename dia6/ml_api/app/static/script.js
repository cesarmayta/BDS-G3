// API endpoints
const API_BASE_URL = "http://127.0.0.1:5000/api/housing"

// DOM Elements
const housingForm = document.getElementById("housing-form")
const housingTable = document.getElementById("housing-table")
const housingData = document.getElementById("housing-data")
const noDataMessage = document.getElementById("no-data-message")
const loadingIndicator = document.getElementById("loading")

// Modal Elements
const editModal = document.getElementById("edit-modal")
const editForm = document.getElementById("edit-form")
const editId = document.getElementById("edit-id")
const editRooms = document.getElementById("edit-rooms")
const closeModalBtn = document.querySelector(".close")

// Confirmation Modal Elements
const confirmModal = document.getElementById("confirm-modal")
const confirmDeleteBtn = document.getElementById("confirm-delete")
const cancelDeleteBtn = document.getElementById("cancel-delete")
let housingToDelete = null

// Toast Notification
const toast = document.getElementById("toast")
const toastMessage = document.getElementById("toast-message")

// Event Listeners
document.addEventListener("DOMContentLoaded", fetchHousingData)
housingForm.addEventListener("submit", addHousing)
editForm.addEventListener("submit", updateHousing)
closeModalBtn.addEventListener("click", closeModal)
confirmDeleteBtn.addEventListener("click", confirmDelete)
cancelDeleteBtn.addEventListener("click", closeConfirmModal)

// Fetch all housing data
async function fetchHousingData() {
  showLoading()
  try {
    const response = await fetch(API_BASE_URL)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }
    const data = await response.json()
    console.log(data.content)
    renderHousingData(data.content)
  } catch (error) {
    console.error("Error fetching housing data:", error)
    showToast("Failed to load housing data. Please try again.", true)
  } finally {
    hideLoading()
  }
}

// Render housing data to table
function renderHousingData(data) {
  housingData.innerHTML = ""

  if (!data || data.length === 0) {
    noDataMessage.classList.remove("hidden")
    housingTable.classList.add("hidden")
    return
  }

  noDataMessage.classList.add("hidden")
  housingTable.classList.remove("hidden")

  data.forEach((housing) => {
    const row = document.createElement("tr")
    row.innerHTML = `
            <td>${housing.id}</td>
            <td>${housing.rooms}</td>
            <td>${housing.price ? "$" + housing.price.toFixed(2) : "Calculated"}</td>
            <td>
                <button class="btn btn-edit" data-id="${housing.id}" data-rooms="${housing.rooms}">Edit</button>
                <button class="btn btn-delete" data-id="${housing.id}">Delete</button>
            </td>
        `
    housingData.appendChild(row)
  })

  // Add event listeners to edit and delete buttons
  document.querySelectorAll(".btn-edit").forEach((button) => {
    button.addEventListener("click", openEditModal)
  })

  document.querySelectorAll(".btn-delete").forEach((button) => {
    button.addEventListener("click", openDeleteConfirmation)
  })
}

// Add new housing
async function addHousing(e) {
  e.preventDefault()

  const rooms = document.getElementById("rooms").value

  if (!rooms) {
    showToast("Please enter the number of rooms", true)
    return
  }

  const housingData = {
    rooms: Number.parseInt(rooms),
  }

  try {
    const response = await fetch(API_BASE_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(housingData),
    })

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }

    showToast("Housing added successfully!")
    housingForm.reset()
    fetchHousingData()
  } catch (error) {
    console.error("Error adding housing:", error)
    showToast("Failed to add housing. Please try again.", true)
  }
}

// Open edit modal
function openEditModal() {
  const id = this.getAttribute("data-id")
  const rooms = this.getAttribute("data-rooms")

  editId.value = id
  editRooms.value = rooms

  editModal.style.display = "block"
}

// Close edit modal
function closeModal() {
  editModal.style.display = "none"
}

// Update housing
async function updateHousing(e) {
  e.preventDefault()

  const id = editId.value
  const rooms = editRooms.value

  if (!rooms) {
    showToast("Please enter the number of rooms", true)
    return
  }

  const housingData = {
    rooms: Number.parseInt(rooms),
  }

  try {
    const response = await fetch(`${API_BASE_URL}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(housingData),
    })

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }

    closeModal()
    showToast("Housing updated successfully!")
    fetchHousingData()
  } catch (error) {
    console.error("Error updating housing:", error)
    showToast("Failed to update housing. Please try again.", true)
  }
}

// Open delete confirmation modal
function openDeleteConfirmation() {
  housingToDelete = this.getAttribute("data-id")
  confirmModal.style.display = "block"
}

// Close confirmation modal
function closeConfirmModal() {
  confirmModal.style.display = "none"
  housingToDelete = null
}

// Confirm delete
async function confirmDelete() {
  if (!housingToDelete) return

  try {
    const response = await fetch(`${API_BASE_URL}/${housingToDelete}`, {
      method: "DELETE",
    })

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }

    closeConfirmModal()
    showToast("Housing deleted successfully!")
    fetchHousingData()
  } catch (error) {
    console.error("Error deleting housing:", error)
    showToast("Failed to delete housing. Please try again.", true)
  }
}

// Show toast notification
function showToast(message, isError = false) {
  toastMessage.textContent = message

  if (isError) {
    toast.classList.add("error")
  } else {
    toast.classList.remove("error")
  }

  toast.classList.add("show")

  setTimeout(() => {
    toast.classList.remove("show")
  }, 3000)
}

// Show loading indicator
function showLoading() {
  loadingIndicator.classList.remove("hidden")
  housingTable.classList.add("hidden")
  noDataMessage.classList.add("hidden")
}

// Hide loading indicator
function hideLoading() {
  loadingIndicator.classList.add("hidden")
}

// Close modals when clicking outside
window.onclick = (event) => {
  if (event.target === editModal) {
    closeModal()
  }
  if (event.target === confirmModal) {
    closeConfirmModal()
  }
}
