package com.example.resumeenhancer.data

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "resumes")
data class ResumeEntity(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val name: String,
    val education: String,
    val projects: String,
    val experience: String,
    val achievements: String,
    val skills: String,
    val targetCompany: String,
    val targetRole: String
)
