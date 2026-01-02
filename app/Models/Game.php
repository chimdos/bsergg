<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Game extends Model
{
    public function brawlMatch()
    {
        return $this->belongsTo(BrawlMatch::class);
    }

    public function performances()
    {
        return $this->hasMany(Performance::class);
    }
}
