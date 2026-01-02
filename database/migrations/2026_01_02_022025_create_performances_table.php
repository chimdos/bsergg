<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('performances', function (Blueprint $table) {
            $table->id();
            $table->foreignId('game_id')->constrained()->onDelete('cascade');
            $table->foreignId('player_id')->constrained();
            $table->string('brawler_name');

            $table->integer('kills')->default(0);
            $table->integer('deaths')->default(value:0);
            $table->integer('damage_dealt')->default(0);
            $table->integer('damage_received')->default(0);
            $table->integer('damage_to_safe')->default(0);

            $table->decimal('rating_bser', 5, 2)->default(0.00);
            $table->boolean('is_win')->default(true);

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('performances');
    }
};
